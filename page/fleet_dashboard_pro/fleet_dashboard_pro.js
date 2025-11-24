
frappe.pages['fleet-dashboard-pro'].on_page_load = function(wrapper) {
  var page = frappe.ui.make_app_page({
    parent: wrapper,
    title: 'Fleet Dashboard Pro',
    single_column: true
  });

  $(frappe.render_template("fleet_dashboard_pro", {})).appendTo(page.body);

  console.log("Dashboard Pro Loaded");
};
