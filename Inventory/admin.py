from django.contrib import admin
from .models import Supplier, Component, PurchaseRequisition, PurchaseOrder, ReplenishTransaction, ConsumptionTransaction

# Custom admin class for Component model
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity', 'reorder_level', 'unit_of_measure', 'supplier', 'cost')
    search_fields = ('name', 'description', 'unit_of_measure', 'supplier__name')
    list_filter = ('unit_of_measure', 'supplier')
    ordering = ('name',)

# Custom admin class for PurchaseRequisition model
class PurchaseRequisitionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'component', 'quantity', 'status', 'created_at', 'updated_at')
    search_fields = ('component__name', 'notes')
    list_filter = ('status', 'created_at', 'updated_at')

# Register your models with the admin site
admin.site.register(Component, ComponentAdmin)
admin.site.register(PurchaseRequisition, PurchaseRequisitionAdmin)
admin.site.register(PurchaseOrder)
admin.site.register(ReplenishTransaction)  # Corrected class name
admin.site.register(ConsumptionTransaction)
admin.site.register(Supplier)
