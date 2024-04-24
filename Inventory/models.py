from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _

class Component(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class PurchaseRequisition(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')

    def __str__(self):
        return f"Purchase Requisition for {self.component} - Quantity: {self.quantity}"

class PurchaseOrder(models.Model):
    purchase_requisition = models.ForeignKey(PurchaseRequisition, on_delete=models.CASCADE)
    purchase_manager_approval = models.BooleanField(default=False)

    def __str__(self):
        return f"Purchase Order for {self.purchase_requisition.component} - Quantity: {self.purchase_requisition.quantity}"

class InventoryTransaction(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_type = models.CharField(max_length=20, choices=[('purchase', 'Purchase'), ('consumption', 'Consumption'), ('scrapping', 'Scrapping')])
    related_document = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type.capitalize()} of {self.quantity} {self.component} at {self.timestamp}"
