frappe.pages['Electricity Distribution'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		// title: 'About Us',
		single_column: true
	});
	//$("<div class='perm-engine' style='min-height: 1px; padding: 15px;'></div>").appendTo(page.main);





	$(frappe.render_template("elec", {})).appendTo(page.main);
}