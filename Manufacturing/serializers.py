# Serializers for Manufacturing app
from rest_framework import serializers
from .models import ManufacturingOrder, MaterialRequisition, BillOfMaterial, BOMItem
from Inventory.models import Component, Supplier, PurchaseRequisition, PurchaseOrder, InventoryTransaction
from Sales.models import SalesOrderItem
from Inventory.serializers import ComponentSerializer
from django.shortcuts import get_object_or_404


class BOMItemSerializer(serializers.ModelSerializer):
    component = ComponentSerializer(read_only=True)
    class Meta:
        model = BOMItem
        fields = '__all__'

class BillOfMaterialSerializer(serializers.ModelSerializer):
    bom_items = BOMItemSerializer(many=True, read_only=True)
    class Meta:
        model = BillOfMaterial
        fields = '__all__'




class MaterialRequisitionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialRequisitionItem
        fields = ['id', 'component', 'quantity']

class MaterialRequisitionSerializer(serializers.ModelSerializer):
    items = MaterialRequisitionItemSerializer(many=True, read_only=True)

    class Meta:
        model = MaterialRequisition
        fields = ['id', 'manufacturing_order', 'created_at', 'updated_at', 'items']



class ManufacturingOrderSerializer(serializers.ModelSerializer):
    sales_order_item = serializers.PrimaryKeyRelatedField(queryset=SalesOrderItem.objects.all(), required=False, allow_null=True)


    class Meta:
        model = ManufacturingOrder
        fields = ['id', 'product_id', 'quantity', 'bom', 'status', 'created_at', 'updated_at', 'sales_order_item']
        read_only_fields = ['product_name']

    def create(self, validated_data):
        print(f"Validated data: {validated_data}")
        return ManufacturingOrder.objects.create(**validated_data)
