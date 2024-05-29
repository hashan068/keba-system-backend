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
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(f"Request data: {request.data}")

        if serializer.is_valid():
            print("Serializer is valid")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Serializer errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        serializer = self.get_serializer(data=request.data)
        print(f"Request data: {request.data}")

        if serializer.is_valid():
            print("Serializer is valid")
            try:
                with transaction.atomic():
                    component_id = serializer.validated_data['component_id'].id
                    quantity = serializer.validated_data['quantity']
                    component = get_object_or_404(Component, id=component_id)

                    try:
                        update_component_quantity(component_id, quantity)
                    except Exception as e:
                        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

                    consumption_transaction = serializer.save()

                    # update_material_requisition_status(consumption_transaction.material_requisition_item.material_requisition)
                    # update_manufacturing_order_status(consumption_transaction.material_requisition_item.material_requisition.manufacturing_order)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                print(f"An exception occurred: {str(e)}")
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)