# Copyright (c) 2026, Dharsh and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    filters = filters or {}

    columns = [
        {
            "label": "Student Name",
            "fieldname": "s_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Department",
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
            "label": "Roll Number",
            "fieldname": "rno",
            "fieldtype": "Data",
            "width": 180
        }
    ]

    conditions = {}

    if filters.get("department"):
        conditions["department"] = filters.get("department")

    data = frappe.get_all(
        "Student",
        filters=conditions,
        fields=[
            "s_name",
            "department",
            "cgpa",
            "rno"
        ]
    )

    return columns, data