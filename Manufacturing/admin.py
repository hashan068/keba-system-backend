from django.contrib import admin
from .models import ManufacturingOrder, MaterialRequisition, BillOfMaterial, BOMItem


# Register your models here.
admin.site.register(ManufacturingOrder)
admin.site.register(MaterialRequisition)
admin.site.register(BillOfMaterial)
admin.site.register(BOMItem)