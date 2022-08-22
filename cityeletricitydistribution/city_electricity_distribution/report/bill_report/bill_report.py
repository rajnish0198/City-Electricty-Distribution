# Copyright (c) 2022, Rajnish Yadav and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns, data = [], []
	return get_column(), get_data(filters)

def get_column():
	columns = ["Consumer Details","Bill No","Bill Date","Consumer Type","Payment Amount","Payment Date","Incentive up to Date"]
	

	return columns

def get_data(filters):
	data =frappe.get_all("Consumer Bill",filters=filters,fields=["consumer_details","bill_no","bill_date","consumer_type","payment_amount","payment_date","incentive_up_to_date"])

	return data

