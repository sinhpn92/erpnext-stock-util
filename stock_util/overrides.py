import frappe
from frappe import _
from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry



class CustomStockEntry(StockEntry):
    def validate_qty(self):
        frappe.throw(_("--->>>>CustomStockEntry:validate_qty---1").format())
        pass