from rest_framework import viewsets
from .models import Component, PurchaseRequisition, MaterialRequisition, MaterialRequisitionItem, PurchaseOrder, InventoryTransaction, Supplier
from .serializers import ComponentSerializer, PurchaseRequisitionSerializer, MaterialRequisitionSerializer, MaterialRequisitionItemSerializer, PurchaseOrderSerializer, InventoryTransactionSerializer, SupplierSerializer
from rest_framework.response import Response
from rest_framework import status

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(f"Request data: {request.data}")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseRequisitionViewSet(viewsets.ModelViewSet):
    queryset = PurchaseRequisition.objects.all()
    serializer_class = PurchaseRequisitionSerializer

class MaterialRequisitionViewSet(viewsets.ModelViewSet):
    queryset = MaterialRequisition.objects.all()
    serializer_class = MaterialRequisitionSerializer

class MaterialRequisitionItemViewSet(viewsets.ModelViewSet):
    queryset = MaterialRequisitionItem.objects.all()
    serializer_class = MaterialRequisitionItemSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class InventoryTransactionViewSet(viewsets.ModelViewSet):
    queryset = InventoryTransaction.objects.all()
    serializer_class = InventoryTransactionSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer