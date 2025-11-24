import frappe

def after_save(doc, method):
    if doc.hour_meter_reading < doc.lasthour_meter_reading:
        frappe.throw("قراءة العداد الحالية يجب أن تكون أكبر من السابقة")

    doc.hours_run = doc.hour_meter_reading - doc.lasthour_meter_reading

    frappe.db.set_value("Fueling Log", doc.name, "lasthour_meter_reading", doc.hour_meter_reading)

    doc.hours_since_maintenance = doc.hour_meter_reading - doc.last_maintenance_reading
    doc.db_update()

    settings = frappe.get_single("SDC Fleet Settings")
    threshold = settings.maintenance_threshold_hours or 300

    if doc.hours_since_maintenance >= threshold:
        create_maintenance_request(doc)

def check_stock(item_code):
    qty = frappe.db.get_value("Bin", {"item_code": item_code}, "actual_qty")
    return qty if qty else 0

def create_maintenance_request(doc):
    existing = frappe.db.exists(
        "Maintenance Request",
        {"asset": doc.asset, "workflow_state": ["in", ["Pending", "Approved"]]}
    )
    if existing:
        return

    mr = frappe.get_doc({
        "doctype": "Maintenance Request",
        "asset": doc.asset,
        "reading_at_request": doc.hour_meter_reading,
        "hours_since_maintenance": doc.hours_since_maintenance,
        "status": "Pending"
    })

    items = frappe.get_all(
        "Equipment Spare Part",
        filters={"parent": doc.asset},
        fields=["item_code", "qty"]
    )

    for item in items:
        mr.append("required_parts", {
            "item_code": item.item_code,
            "qty": item.qty,
            "available": check_stock(item.item_code)
        })

    mr.insert()
    frappe.db.commit()
