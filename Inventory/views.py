from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from .models import Component, PurchaseRequisition, PurchaseOrder, ReplenishTransaction, ConsumptionTransaction, Supplier

from .serializers import ComponentSerializer, PurchaseRequisitionSerializer, PurchaseOrderSerializer,  SupplierSerializer, ReplenishTransactionSerializer, ConsumptionTransactionSerializer
from Manufacturing.models import MaterialRequisitionItem

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

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ReplenishTransactionViewSet(viewsets.ModelViewSet):
    queryset = ReplenishTransaction.objects.all()
    serializer_class = ReplenishTransactionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class ConsumptionTransactionViewSet(viewsets.ModelViewSet):
    queryset = ConsumptionTransaction.objects.all()
    serializer_class = ConsumptionTransactionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class ConsumptionTransactionViewSet(viewsets.ModelViewSet):
#     queryset = ConsumptionTransaction.objects.all()
#     serializer_class = ConsumptionTransactionSerializer

#     def create(self, request, *args, **kwargs):
#         print("Received request data:", request.data)  # Print request data for debugging
        
#         serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        
#         if serializer.is_valid():
#             print("Serializer is valid, data:", serializer.validated_data)  # Print validated data for debugging
#             self.perform_create(serializer)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print("Serializer is not valid, errors:", serializer.errors)  # Print errors for debugging
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def perform_create(self, serializer):
#         serializer.save()