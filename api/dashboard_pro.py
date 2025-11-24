
import frappe

@frappe.whitelist()
def get_kpis():
    return {"total_assets":10,"active":8,"needs_maintenance":2}

@frappe.whitelist()
def get_fuel_charts():
    return {}

@frappe.whitelist()
def get_maintenance_charts():
    return {}

@frappe.whitelist()
def get_equipment_status():
    return []

@frappe.whitelist()
def get_asset_profile(asset):
    return {}
