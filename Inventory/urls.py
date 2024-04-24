from django.urls import path
from .views import (
    ComponentListCreateView,
    ComponentRetrieveUpdateDestroyView,
    PurchaseRequisitionListCreateView,
    PurchaseRequisitionRetrieveUpdateDestroyView,

)

urlpatterns = [
    path('components/', ComponentListCreateView.as_view(), name='component-list-create'),
    path('components/<int:pk>/', ComponentRetrieveUpdateDestroyView.as_view(), name='component-retrieve-update-destroy'),
    path('purchase-requisitions/', PurchaseRequisitionListCreateView.as_view(), name='purchase-requisition-list-create'),
    path('purchase-requisitions/<int:pk>/', PurchaseRequisitionRetrieveUpdateDestroyView.as_view(), name='purchase-requisition-retrieve-update-destroy'),

]
