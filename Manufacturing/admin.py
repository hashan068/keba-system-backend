from django.contrib import admin
from .models import ManufacturingOrder, MaterialRequisition, BillOfMaterial, BOMItem, MaterialRequisitionItem

# Register your models here.

class MaterialRequisitionItemInline(admin.TabularInline):
    model = MaterialRequisitionItem
    extra = 0

class MaterialRequisitionAdmin(admin.ModelAdmin):
    inlines = [MaterialRequisitionItemInline]
    list_display = ('id', 'manufacturing_order', 'bom', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('manufacturing_order__id',)

class BOMItemInline(admin.TabularInline):
    model = BOMItem
    extra = 0

class BillOfMaterialAdmin(admin.ModelAdmin):
    inlines = [BOMItemInline]
    list_display = ('name', 'product', 'created_at', 'updated_at')
    search_fields = ('name', 'product__name')

admin.site.register(ManufacturingOrder)
admin.site.register(MaterialRequisition, MaterialRequisitionAdmin)
admin.site.register(BillOfMaterial, BillOfMaterialAdmin)