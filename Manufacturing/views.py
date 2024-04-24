from rest_framework import viewsets
from .models import ManufacturingOrder, MaterialRequisition, BillOfMaterial, BOMItem
from .serializers import ManufacturingOrderSerializer, MaterialRequisitionSerializer, BillOfMaterialSerializer, BOMItemSerializer

class ManufacturingOrderViewSet(viewsets.ModelViewSet):
    queryset = ManufacturingOrder.objects.all()
    serializer_class = ManufacturingOrderSerializer

class MaterialRequisitionViewSet(viewsets.ModelViewSet):
    queryset = MaterialRequisition.objects.all()
    serializer_class = MaterialRequisitionSerializer

class BillOfMaterialViewSet(viewsets.ModelViewSet):
    queryset = BillOfMaterial.objects.all()
    serializer_class = BillOfMaterialSerializer

class BOMItemViewSet(viewsets.ModelViewSet):
    queryset = BOMItem.objects.all()
    serializer_class = BOMItemSerializer
