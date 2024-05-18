from django.contrib import admin
from .models import Customer, Product, Quotation, SalesOrder, SalesOrderItem

# Custom admin class for Customer model
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'email', 'phone', 'address')

    ordering = ('name',)

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(SalesOrder)
admin.site.register(SalesOrderItem)
admin.site.register(Quotation)
# admin.site.register(RFQs)

