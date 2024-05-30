from django.contrib import admin
from .models import Customer, Product, Quotation, QuotationItem, SalesOrder, SalesOrderItem, RFQ, RFQItem

# Custom admin class for Customer model
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'email', 'phone', 'address')
    ordering = ('name',)
    list_per_page = 10

# Custom admin class for RFQ model
class RFQAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'creator', 'created_at', 'updated_at', 'status', 'due_date')
    search_fields = ('creator__username', 'description')
    list_filter = ('status', 'created_at', 'updated_at')
    ordering = ('-created_at',)

# Custom admin class for RFQItem model
class RFQItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'rfq', 'product', 'quantity', 'unit_price')
    search_fields = ('rfq__id', 'product__name')
    ordering = ('rfq',)

# Custom admin class for Quotation model
class QuotationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'customer', 'date', 'expiration_date', 'total_amount', 'status', 'created_at', 'updated_at', 'created_by')
    search_fields = ('customer__name', 'created_by__username')
    list_filter = ('status', 'created_at', 'updated_at')
    ordering = ('-created_at',)

# Custom admin class for QuotationItem model
class QuotationItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'quotation', 'product', 'quantity', 'unit_price')
    search_fields = ('quotation__id', 'product__name')
    ordering = ('quotation',)

# Custom admin class for SalesOrder model
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'customer', 'total_amount', 'status', 'created_at', 'updated_at')
    search_fields = ('customer__name',)
    list_filter = ('status', 'created_at', 'updated_at')
    ordering = ('-created_at',)

# Custom admin class for SalesOrderItem model
class SalesOrderItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__name')
    ordering = ('order',)

# Register your models with the admin site
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(RFQ, RFQAdmin)
admin.site.register(RFQItem, RFQItemAdmin)
admin.site.register(Quotation, QuotationAdmin)
admin.site.register(QuotationItem, QuotationItemAdmin)
admin.site.register(SalesOrder, SalesOrderAdmin)
admin.site.register(SalesOrderItem, SalesOrderItemAdmin)