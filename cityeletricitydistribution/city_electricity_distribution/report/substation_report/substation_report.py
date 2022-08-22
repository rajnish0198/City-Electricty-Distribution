# Copyright (c) 2022, Rajnish Yadav and contributors
# For license information, please see license.txt

#import frappe
#from numpy import column_stack

def execute(filters=None):
	columns, data = [], []
	columns = ["substation","core"]
	data =[[1,2],[3,4]]
	return columns,data