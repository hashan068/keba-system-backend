from rest_framework import generics
from .models import Component, PurchaseRequisition, PurchaseOrder, InventoryTransaction
from .serializers import ComponentSerializer, PurchaseRequisitionSerializer, PurchaseOrderSerializer, InventoryTransactionSerializer

class ComponentListCreateView(generics.ListCreateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class ComponentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class PurchaseRequisitionListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseRequisition.objects.all()
    serializer_class = PurchaseRequisitionSerializer

class PurchaseRequisitionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseRequisition.objects.all()
    serializer_class = PurchaseRequisitionSerializer

# Add views for other models similarly


