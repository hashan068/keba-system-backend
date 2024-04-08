from rest_framework import serializers
from .models import Component, PurchaseRequisition, PurchaseOrder, InventoryTransaction, ScrappedManufacturingOrder

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'

class PurchaseRequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRequisition
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class InventoryTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTransaction
        fields = '__all__'

class ScrappedManufacturingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrappedManufacturingOrder
        fields = '__all__'
