from rest_framework import serializers
from .models import ManufacturingOrder, MaterialRequisition, BillOfMaterial, BOMItem

class BOMItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOMItem
        fields = '__all__'

class BillOfMaterialSerializer(serializers.ModelSerializer):
    bom_items = BOMItemSerializer(many=True, read_only=True)

    class Meta:
        model = BillOfMaterial
        fields = '__all__'

class MaterialRequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialRequisition
        fields = '__all__'

class ManufacturingOrderSerializer(serializers.ModelSerializer):
    material_requisitions = MaterialRequisitionSerializer(many=True, read_only=True)
    class Meta:
        model = ManufacturingOrder
        fields = '__all__'
