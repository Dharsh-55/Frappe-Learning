# Copyright (c) 2026, Dharsh and contributors
# For license information, please see license.txt

# import frappe
from frappe import _
import frappe

def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = [
		{
			"label":"Student Name",
			"fieldname": "s_name",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label":"Department",
			"fieldname": "department",
			"fieldtype": "Link",
			"options": "DepartmentX",
			"width": 150
		},
		{
			"label": "CGPA",
			"fieldname": "cgpa",
			"fieldtype": "Float",
			"width": 100
		},
		{
			'label': 'Roll Number',
			'fieldname': 'rno',
			'fieldtype': 'Data',
			'width': 180
		},
		{
			'label': 'standard',
			'fieldname': 'std',
		}
	]

	conditions = {}

	if filters.get("department"):
		conditions["department"] = filters.get("department")

	data = frappe.get_all(
		"Student",
		filters = conditions,
		fields = [
			"s_name",
			"department",
			"cgpa",
		"rno"
		]
	)

	return columns, data


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Column 1"),
			"fieldname": "column_1",
			"fieldtype": "Data",
		},
		{
			"label": _("Column 2"),
			"fieldname": "column_2",
			"fieldtype": "Int",
		},
	]


def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	return [
		["Row 1", 1],
		["Row 2", 2],
	]
