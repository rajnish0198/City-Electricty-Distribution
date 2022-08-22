// Copyright (c) 2022, Rajnish Yadav and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Bill Report"] = {
	"filters": [
		{
			"fieldname":"consumer_details",
			"label": __("Consumer Details"),
			"fieldtype": "Data",
		},
		{
			"fieldname":"consumer_type",
			"label": __("Consumer Type"),
			"fieldtype": "Data",
		},
		{
			"fieldname":"payment_date",
			"label": __("Payment Date"),
			"fieldtype": "Date",
		},
		{
			"fieldname":"bill_date",
			"label": __("Bill Date"),
			"fieldtype": "Date",
		},

	]
};
