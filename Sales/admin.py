from django.contrib import admin
from .models import Customer, Product, SalesOrder, SalesOrderItem

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(SalesOrder)
admin.site.register(SalesOrderItem)
