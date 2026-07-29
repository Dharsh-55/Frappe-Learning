# Copyright (c) 2026, Dharsh and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Assignments(Document):
	def before_save(self):
		if not self.description:
			self.description = "Default Description is written"
