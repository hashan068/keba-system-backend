from django.contrib import admin
from .models import Customer, Product, Quotation, SalesOrder, SalesOrderItem

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(SalesOrder)
admin.site.register(SalesOrderItem)
admin.site.register(Quotation)
# admin.site.register(RFQs)
