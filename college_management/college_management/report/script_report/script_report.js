// Copyright (c) 2026, Dharsh and contributors
// For license information, please see license.txt

frappe.query_reports["Script Report"] = {
	filters: [
		{
			fieldname: "department",
			label: "Department",
			fieldtype: "Link",
			options: "Department"
		},
	],
};
