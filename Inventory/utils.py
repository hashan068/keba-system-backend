# utils.py
from django.db import transaction

from .models import ConsumptionTransaction, Component

from django.shortcuts import get_object_or_404

def get_material_requisition_serializer():
    from Manufacturing.serializers import MaterialRequisitionSerializer
    return MaterialRequisitionSerializer

def get_manufacturing_order_serializer():
    from Manufacturing.serializers import ManufacturingOrderSerializer
    return ManufacturingOrderSerializer

@transaction.atomic
def create_consumption_transaction(validated_data):
    component_id = validated_data['component_id'].id
    quantity = validated_data['quantity']

    component = get_object_or_404(Component, id=component_id)

    if component.quantity < quantity:
        raise Exception(f"Insufficient quantity for component {component.name}. Available quantity: {component.quantity}")

    consumption_transaction = ConsumptionTransaction.objects.create(**validated_data)

    update_component_quantity(component_id, quantity)
    update_material_requisition_status(consumption_transaction.material_requisition_item.material_requisition)
    update_manufacturing_order_status(consumption_transaction.material_requisition_item.material_requisition.manufacturing_order)

    return consumption_transaction

@transaction.atomic
def update_component_quantity(component_id, quantity):
    component = get_object_or_404(Component, id=component_id)
    component.quantity -= quantity  # Reduce the component quantity by the consumed amount
    component.save()

@transaction.atomic
def update_material_requisition_status(material_requisition):
    MaterialRequisitionSerializer = get_material_requisition_serializer()
    serializer = MaterialRequisitionSerializer(material_requisition, data={'status': 'approved'}, partial=True)

    if serializer.is_valid():
        serializer.save()
    else:
        raise Exception(f"Failed to update MaterialRequisition status: {serializer.errors}")

@transaction.atomic
def update_manufacturing_order_status(manufacturing_order):
    ManufacturingOrderSerializer = get_manufacturing_order_serializer()
    serializer = ManufacturingOrderSerializer(manufacturing_order, data={'status': 'mr_approved'}, partial=True)

    if serializer.is_valid():
        serializer.save()
    else:
        raise Exception(f"Failed to update Manaufacturing Order status: {serializer.errors}")