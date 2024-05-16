from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ComponentViewSet,
    PurchaseRequisitionViewSet,
    PurchaseOrderViewSet,
    InventoryTransactionViewSet,
    SupplierViewSet,
)

router = DefaultRouter()
router.register(r'components', ComponentViewSet, basename='component')
router.register(r'purchase-requisitions', PurchaseRequisitionViewSet, basename='purchase-requisition')
router.register(r'purchase-orders', PurchaseOrderViewSet, basename='purchase-order')
router.register(r'inventory-transactions', InventoryTransactionViewSet, basename='inventory-transaction')
router.register(r'suppliers', SupplierViewSet, basename='supplier')

urlpatterns = [
    path('', include(router.urls)),
]