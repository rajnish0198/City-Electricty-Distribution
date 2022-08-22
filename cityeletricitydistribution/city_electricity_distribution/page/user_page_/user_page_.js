frappe.pages['user-page-'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'User',
		single_column: true
	});
	$(frappe.render_template("user", {})).appendTo(page.main);

}