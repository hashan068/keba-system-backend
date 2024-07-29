from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import Component, PurchaseRequisition, PurchaseOrder, ReplenishTransaction, ConsumptionTransaction, Supplier
from django.db import transaction
from django.shortcuts import get_object_or_404
from .serializers import ComponentSerializer, PurchaseRequisitionSerializer, PurchaseOrderSerializer,  SupplierSerializer, ReplenishTransactionSerializer, ConsumptionTransactionSerializer
from Manufacturing.models import MaterialRequisitionItem
from .utils import update_component_quantity

 # Create your views here.
class ComponentViewSet(viewsets.ModelViewSet): 
    queryset = Component.objects.all() # Get all the components
    serializer_class = ComponentSerializer # Use the ComponentSerializer to serialize the data

    def create(self, request, *args, **kwargs): # Create a new component
        serializer = self.get_serializer(data=request.data) # Get the serializer
        print(f"Request data: {request.data}") 
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Return the data if the serializer is valid
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Return the errors if the serializer is not valid

class PurchaseRequisitionViewSet(viewsets.ModelViewSet): # ViewSet for PurchaseRequisition
    queryset = PurchaseRequisition.objects.all() # Get all the purchase requisitions
    serializer_class = PurchaseRequisitionSerializer # Use the PurchaseRequisitionSerializer to serialize the data
    
    def create(self, request, *args, **kwargs): # Create a new purchase requisition
        serializer = self.get_serializer(data=request.data) # Get the serializer
        print(f"Request data: {request.data}")

        if serializer.is_valid():
            print("Serializer is valid") # Check if the serializer is valid
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Return the data if the serializer is valid
        else:
            print("Serializer errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Return the errors if the serializer is not valid

class PurchaseOrderViewSet(viewsets.ModelViewSet): # ViewSet for PurchaseOrder
    queryset = PurchaseOrder.objects.all() # Get all the purchase orders
    serializer_class = PurchaseOrderSerializer # Use the PurchaseOrderSerializer to serialize the data

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ReplenishTransactionViewSet(viewsets.ModelViewSet):
    queryset = ReplenishTransaction.objects.all()
    serializer_class = ReplenishTransactionSerializer

    def create(self, request, *args, **kwargs): # Create a new replenish transaction
        serializer = self.get_serializer(data=request.data) # Get the serializer
        if serializer.is_valid(): # Check if the serializer is valid
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsumptionTransactionViewSet(viewsets.ModelViewSet):
    queryset = ConsumptionTransaction.objects.all()
    serializer_class = ConsumptionTransactionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(f"Request data: {request.data}")

        if serializer.is_valid():
            print("Serializer is valid")
            try:
                consumption_transaction = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except serializers.ValidationError as e:
                return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(f"An exception occurred: {str(e)}")
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)