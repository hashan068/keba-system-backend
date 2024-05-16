from rest_framework import serializers
from .models import Component, PurchaseRequisition, MaterialRequisition, MaterialRequisitionItem, PurchaseOrder, InventoryTransaction, Supplier

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id', 'name', 'description', 'quantity', 'reorder_level', 'unit_of_measure', 'supplier_id', 'cost')

    def create(self, validated_data):
        return Component.objects.create(**validated_data)

class PurchaseRequisitionSerializer(serializers.ModelSerializer):
    component_name = serializers.ReadOnlyField(source='component.name')

    class Meta:
        model = PurchaseRequisition
        fields = ('id', 'creator_id', 'component_id', 'component_name', 'quantity', 'status', 'notes', 'created_at', 'updated_at')

class MaterialRequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialRequisition
        fields = ('id', 'manufacturing_order_id', 'creator_id', 'status', 'notes', 'created_at', 'updated_at')

class MaterialRequisitionItemSerializer(serializers.ModelSerializer):
    component_name = serializers.ReadOnlyField(source='component.name')

    class Meta:
        model = MaterialRequisitionItem
        fields = ('id', 'material_requisition_id', 'component_id', 'component_name', 'quantity')

class PurchaseOrderSerializer(serializers.ModelSerializer):
    purchase_requisition_details = serializers.ReadOnlyField(source='purchase_requisition.__str__')

    class Meta:
        model = PurchaseOrder
        fields = ('id', 'creator_id', 'purchase_requisition_id', 'purchase_requisition_details', 'supplier_id', 'purchase_manager_approval', 'status', 'notes', 'created_at', 'updated_at')

class InventoryTransactionSerializer(serializers.ModelSerializer):
    component_name = serializers.ReadOnlyField(source='component.name')

    class Meta:
        model = InventoryTransaction
        fields = ('id', 'component_id', 'component_name', 'quantity', 'transaction_type', 'related_document', 'timestamp')

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'name', 'email', 'address', 'website', 'date_added', 'is_active', 'notes')