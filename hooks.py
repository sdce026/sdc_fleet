
app_name='sdc_fleet'
app_title='SDC Fleet'
app_publisher='SDCE'
app_email='support@sdce.com'
app_description='Fleet Management System'

doc_events = {
    "Fueling Log": {"after_save": "sdc_fleet.api.fueling.after_save"},
    "Maintenance Log": {"on_submit": "sdc_fleet.api.maintenance.on_submit"}
}


# Added Dashboard Pro
