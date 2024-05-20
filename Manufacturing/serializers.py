# Serializers for Manufacturing app
from rest_framework import serializers
from .models import ManufacturingOrder, MaterialRequisition,MaterialRequisitionItem, BillOfMaterial, BOMItem
from Inventory.models import Component, Supplier, PurchaseRequisition, PurchaseOrder
from Sales.models import SalesOrderItem
from Inventory.serializers import ComponentSerializer
from django.shortcuts import get_object_or_404

class MaterialRequisitionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialRequisitionItem
        fields = ['id', 'component', 'quantity']

class MaterialRequisitionSerializer(serializers.ModelSerializer):
    items = MaterialRequisitionItemSerializer(many=True, read_only=True)

    class Meta:
        model = MaterialRequisition
        fields = ['id', 'manufacturing_order', 'bom', 'status', 'created_at', 'updated_at', 'items']

    def create(self, validated_data):
        manufacturing_order = validated_data['manufacturing_order']
        bom = validated_data.get('bom')

        material_requisition = MaterialRequisition.objects.create(**validated_data)
        items_data = []

        if bom:
            for bom_item in bom.bom_items.all():
                quantity = manufacturing_order.quantity * bom_item.quantity
                item_data = {
                    'material_requisition': material_requisition,
                    'component': bom_item.component,
                    'quantity': quantity
                }
                items_data.append(item_data)
                MaterialRequisitionItem.objects.create(**item_data)
        
        return material_requisition


class BOMItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMItem
        fields = ['id', 'bill_of_material', 'component', 'quantity']
        read_only_fields = ['bill_of_material']


class BillOfMaterialSerializer(serializers.ModelSerializer):
    bom_items = BOMItemSerializer(many=True)
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = BillOfMaterial
        fields = ('id', 'name', 'product', 'product_name', 'bom_items', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def create(self, validated_data):
        bom_items_data = validated_data.pop('bom_items', [])
        bill_of_material = BillOfMaterial.objects.create(**validated_data)

        for bom_item_data in bom_items_data:
            BOMItem.objects.create(bill_of_material=bill_of_material, **bom_item_data)

        return bill_of_material


class ManufacturingOrderSerializer(serializers.ModelSerializer):
    sales_order_item = serializers.PrimaryKeyRelatedField(queryset=SalesOrderItem.objects.all(), required=False, allow_null=True)

    class Meta:
        model = ManufacturingOrder
        fields = ['id', 'product_id', 'quantity', 'bom', 'status', 'created_at', 'updated_at', 'sales_order_item']
        read_only_fields = ['product_name']

    def create(self, validated_data):
        print(f"Validated data: {validated_data}")
        return ManufacturingOrder.objects.create(**validated_data)
