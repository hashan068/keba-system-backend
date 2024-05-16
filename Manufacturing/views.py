# views.py for the Manufacturing app
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ManufacturingOrder, MaterialRequisition, BillOfMaterial, BOMItem
from .serializers import ManufacturingOrderSerializer, MaterialRequisitionSerializer, BillOfMaterialSerializer, BOMItemSerializer
from Sales.models import SalesOrderItem
from Inventory.models import Component


class MaterialRequisitionViewSet(viewsets.ModelViewSet):
    queryset = MaterialRequisition.objects.all()
    serializer_class = MaterialRequisitionSerializer



class BillOfMaterialViewSet(viewsets.ModelViewSet):
    serializer_class = BillOfMaterialSerializer
    queryset = BillOfMaterial.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            bill_of_material = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)  # Add this line to print serializer errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BOMItemViewSet(viewsets.ModelViewSet):
    queryset = BOMItem.objects.all()
    serializer_class = BOMItemSerializer

class ManufacturingOrderViewSet(viewsets.ModelViewSet):
    queryset = ManufacturingOrder.objects.all()
    serializer_class = ManufacturingOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(f"Request data: {request.data}")
        if serializer.is_valid():
            manufacturing_order = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ManufacturingOrderViewSet(viewsets.ModelViewSet):
#     queryset = ManufacturingOrder.objects.all()
#     serializer_class = ManufacturingOrderSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         print(f"Request data: {request.data}")
#         if serializer.is_valid():
#             SalesOrderItem = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        