from django.contrib import admin
from .models import Component, PurchaseRequisition, PurchaseOrder, InventoryTransaction, Supplier

# Register your models here.
admin.site.register(Component)
admin.site.register(PurchaseRequisition)
admin.site.register(PurchaseOrder)
admin.site.register(InventoryTransaction)
admin.site.register(Supplier)
