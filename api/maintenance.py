import frappe

def on_submit(doc, method):
    frappe.db.set_value(
        "Fueling Log",
        {"asset": doc.asset},
        "last_maintenance_reading",
        doc.hour_meter_reading
    )

    open_requests = frappe.get_all(
        "Maintenance Request",
        filters={"asset": doc.asset, "workflow_state": ["in", ["Pending", "Approved"]]}
    )

    for req in open_requests:
        frappe.db.set_value("Maintenance Request", req.name, "workflow_state", "Completed")
