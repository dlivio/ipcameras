# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ipcameras"
app_title = "IPCameras"
app_publisher = "Diogo Livio"
app_description = "App to control and view the stream of Dahua IPCameras setup streaming in MJPEG format by using a proxy server built in NodeJS to authenticate using Digest Authentication."
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "d.livio@campus.fct.unl.pt"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ipcameras/css/ipcameras.css"
# app_include_js = "/assets/ipcameras/js/ipcameras.js"

# include js, css files in header of web template
# web_include_css = "/assets/ipcameras/css/ipcameras.css"
# web_include_js = "/assets/ipcameras/js/ipcameras.js"

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
# get_website_user_home_page = "ipcameras.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ipcameras.install.before_install"
# after_install = "ipcameras.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ipcameras.notifications.get_notification_config"

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
# 		"ipcameras.tasks.all"
# 	],
# 	"daily": [
# 		"ipcameras.tasks.daily"
# 	],
# 	"hourly": [
# 		"ipcameras.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ipcameras.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ipcameras.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ipcameras.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ipcameras.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ipcameras.task.get_dashboard_data"
# }

