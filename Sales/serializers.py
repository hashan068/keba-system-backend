from rest_framework import serializers
from decimal import Decimal
from datetime import datetime
from django.utils.timezone import make_aware
import pytz
from .models import Customer, Product, RFQ, RFQItem, SalesOrder, SalesOrderItem, Quotation, QuotationItem


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class RFQItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RFQItem
        fields = ('id', 'rfq', 'product', 'quantity', 'unit_price')

class RFQSerializer(serializers.ModelSerializer):
    items = RFQItemSerializer(many=True, read_only=True)

    class Meta:
        model = RFQ
        fields = ('id', 'creator', 'created_at', 'updated_at', 'status', 'due_date', 'description', 'items')

# serializers.py
class QuotationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationItem
        fields = ['product', 'quantity', 'unit_price']

class QuotationSerializer(serializers.ModelSerializer):
    quotation_items = QuotationItemSerializer(many=True)
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    date = serializers.DateField(format='%Y-%m-%d')
    expiration_date = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Quotation
        fields = ['id', 'customer', 'customer_name', 'date', 'expiration_date', 'invoicing_and_shipping_address', 'total_amount', 'status', 'quotation_items']

    def get_date(self, obj):
        return obj.date.strftime('%Y-%m-%d')

    def get_expiration_date(self, obj):
        return obj.expiration_date.strftime('%Y-%m-%d')
        
    def create(self, validated_data):
        quotation_items_data = validated_data.pop('quotation_items')
        total_amount = sum(item['quantity'] * item['unit_price'] for item in quotation_items_data)
        validated_data['total_amount'] = total_amount

        quotation = Quotation.objects.create(**validated_data)
        for quotation_item_data in quotation_items_data:
            QuotationItem.objects.create(quotation=quotation, **quotation_item_data)
        return quotation


class SalesOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderItem
        fields = ['product', 'quantity', 'price']
        

class SalesOrderSerializer(serializers.ModelSerializer):
    order_items = SalesOrderItemSerializer(many=True)
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    class Meta:
        model = SalesOrder
        fields = ['id', 'customer', 'customer_name', 'order_items', 'total_amount', 'status', 'created_at', 'updated_at']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')

        total_amount = sum(Decimal(item['price']) * item['quantity'] for item in order_items_data)
        validated_data['total_amount'] = total_amount

        sales_order = SalesOrder.objects.create(**validated_data)

        for order_item_data in order_items_data:
            SalesOrderItem.objects.create(order=sales_order, **order_item_data)

        return sales_order

    # def create(self, validated_data):
    #     quotation_items_data = validated_data.pop('quotation_items')
    #     total_amount = sum(item['quantity'] * item['unit_price'] for item in quotation_items_data)
    #     validated_data['total_amount'] = total_amount

    #     quotation = Quotation.objects.create(**validated_data)

    #     for quotation_item_data in quotation_items_data:
    #         QuotationItem.objects.create(quotation=quotation, **quotation_item_data)

    #     return quotation