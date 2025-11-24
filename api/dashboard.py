import frappe

@frappe.whitelist()
def get_dashboard_data(asset):
    total_fuel = frappe.db.sql(
        "SELECT SUM(fuel_qty) FROM `tabFueling Log` WHERE asset=%s", (asset,)
    )[0][0]

    total_hours = frappe.db.sql(
        "SELECT SUM(hours_run) FROM `tabFueling Log` WHERE asset=%s", (asset,)
    )[0][0]

    return {
        "total_fuel": total_fuel or 0,
        "total_hours": total_hours or 0,
        "fuel_per_hour": (total_fuel / total_hours) if total_hours else 0
    }
