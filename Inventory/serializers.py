from rest_framework import serializers
from .models import Component, PurchaseRequisition, PurchaseOrder, ReplenishTransaction, ConsumptionTransaction, Supplier
from django.db import transaction

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .utils import update_component_quantity

User = get_user_model()

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id', 'name', 'description', 'quantity','reorder_quantity', 'reorder_level', 'unit_of_measure', 'supplier_id', 'cost')

    def create(self, validated_data):
        return Component.objects.create(**validated_data)


class PurchaseRequisitionSerializer(serializers.ModelSerializer):
    component_id = serializers.PrimaryKeyRelatedField(queryset=Component.objects.all(), source='component')

    class Meta:
        model = PurchaseRequisition
        fields = ('id', 'component_id', 'quantity', 'notes', 'priority', 'status', 'created_at')

    def create(self, validated_data):
        component_data = validated_data.pop('component')
        component = Component.objects.get(id=component_data.id)
        purchase_requisition = PurchaseRequisition.objects.create(component=component, **validated_data)
        return purchase_requisition

class PurchaseOrderSerializer(serializers.ModelSerializer):
    purchase_requisition_details = serializers.ReadOnlyField(source='purchase_requisition.__str__')

    class Meta:
        model = PurchaseOrder
        fields = ('id', 'creator_id', 'purchase_requisition_id', 'purchase_requisition_details', 'supplier_id', 'purchase_manager_approval', 'status', 'notes', 'created_at', 'updated_at')

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'name', 'email', 'address', 'website', 'date_added', 'is_active', 'notes')

class ReplenishTransactionSerializer(serializers.ModelSerializer):
    component_name = serializers.ReadOnlyField(source='component.name')
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ReplenishTransaction
        fields = ('id', 'purchase_requisition', 'component', 'component_name', 'quantity', 'user', 'user_name', 'timestamp')


class ConsumptionTransactionSerializer(serializers.ModelSerializer):
    component_name = serializers.ReadOnlyField(source='component_id.name')
    user_name = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = ConsumptionTransaction
        fields = ('id', 'material_requisition_item', 'component_id', 'component_name', 'quantity', 'user_id', 'user_name', 'timestamp')



