# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "samba_pos_integration"
app_title = "Samba Pos Integration"
app_publisher = "Adam"
app_description = "Samba Pos Integration with ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "adam.daveed@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/samba_pos_integration/css/samba_pos_integration.css"
# app_include_js = "/assets/samba_pos_integration/js/samba_pos_integration.js"

# include js, css files in header of web template
# web_include_css = "/assets/samba_pos_integration/css/samba_pos_integration.css"
# web_include_js = "/assets/samba_pos_integration/js/samba_pos_integration.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "samba_pos_integration.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "samba_pos_integration.install.before_install"
# after_install = "samba_pos_integration.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "samba_pos_integration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"samba_pos_integration.tasks.all"
# 	],
# 	"daily": [
# 		"samba_pos_integration.tasks.daily"
# 	],
# 	"hourly": [
# 		"samba_pos_integration.tasks.hourly"
# 	],
# 	"weekly": [
# 		"samba_pos_integration.tasks.weekly"
# 	]
# 	"monthly": [
# 		"samba_pos_integration.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "samba_pos_integration.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "samba_pos_integration.event.get_events"
# }

