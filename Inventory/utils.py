# utils.py
from django.db import transaction
from .models import ConsumptionTransaction, Component
from django.shortcuts import get_object_or_404

def get_material_requisition_serializer():
    from Manufacturing.serializers import MaterialRequisitionSerializer
    return MaterialRequisitionSerializer

@transaction.atomic
def create_consumption_transaction(validated_data):
    consumption_transaction = ConsumptionTransaction.objects.create(**validated_data)
    update_component_quantity(consumption_transaction.component_id.id, consumption_transaction.quantity)
    update_material_requisition_status(consumption_transaction.material_requisition_item.material_requisition)
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