# Copyright (c) 2022, Rajnish Yadav and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ConsumerBill(Document):
	
   def before_save(self):
	    frappe.msgprint("Bill Generate")

# @frappe.whitelist()
# def before_save():
# 	a = frappe.get_single('City Electricity Setting').per_unit_charge_for_residential
# 	frappe.msgprint(a)