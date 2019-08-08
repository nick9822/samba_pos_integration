# -*- coding: utf-8 -*-
# Copyright (c) 2019, GoElite and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import datetime, frappe, redis, ast
from frappe import msgprint, _

class SambaUtilities():
	pass

@frappe.whitelist()
def submit_samba_invoices():
    draft_invoices = frappe.get_list("Sales Invoice", filters=[["from_sambapos", "=", "1"], ["status", "=", "Draft"]], fields=["name"])
    for e in draft_invoices:
        inv = frappe.get_doc("Sales Invoice", e.name)
        inv.auto_submit_attempted = 1
        inv.save()
        try:
            inv.submit()
        except:
            continue
        frappe.db.commit()