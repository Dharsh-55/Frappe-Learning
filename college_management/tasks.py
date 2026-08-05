import frappe
def daily_maintenance():
    frappe.log_error(
        title = "daily maintenance",
        message = " daily maintenance job executed successfully"
    )