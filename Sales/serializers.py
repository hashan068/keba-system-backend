from rest_framework import serializers
from decimal import Decimal

from .models import Customer, Product, SalesOrder, SalesOrderItem

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SalesOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderItem
        fields = ['product', 'quantity', 'price']
        

class SalesOrderSerializer(serializers.ModelSerializer):
    order_items = SalesOrderItemSerializer(many=True)

    class Meta:
        model = SalesOrder
        fields = ['id', 'customer', 'order_items', 'total_amount', 'status', 'created_at', 'updated_at']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')

        total_amount = sum(Decimal(item['price']) * item['quantity'] for item in order_items_data)
        validated_data['total_amount'] = total_amount

        sales_order = SalesOrder.objects.create(**validated_data)

        for order_item_data in order_items_data:
            SalesOrderItem.objects.create(order=sales_order, **order_item_data)

        return sales_order

