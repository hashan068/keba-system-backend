# sales/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# Register the viewsets for the API endpoints
router.register(r'customers', views.CustomerViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.SalesOrderViewSet)
router.register(r'order-items', views.SalesOrderItemViewSet)

urlpatterns = [
    # Include the API endpoints in the URL patterns
    path('', include(router.urls)),
]