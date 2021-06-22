from __future__ import unicode_literals
import frappe
from frappe import _
import frappe.www.list

no_cache = 1

def get_context(context):
	if frappe.session.user=='Guest':
		frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)

	context.show_sidebar=True
	"""
	user = frappe.get_doc('User', frappe.session.user)
	print('OLA')
	print(user.ipcam_links[0].link)
	"""
	#get_current_user_links()
	

def get_current_user_links():
	"""Returns the links of the current client from frappe.session.user

	Returns:
		object: list of links of the current user
	"""
	email = frappe.session.user
	links = []

	if email in ('Administrator', 'Guest'):
		return None
	
	print('OLA')
	
	try:
		user = frappe.get_doc('User', email)

		for element in user.ipcam_links:
			links.append(element.link)
			print(element.link)

		return links
	except (IndexError, frappe.DoesNotExistError):
		return None