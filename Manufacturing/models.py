from django.db import models
from Sales.models import SalesOrder
from django.utils.translation import gettext_lazy as _

class ManufacturingOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', _('Pending')),
        ('in_progress', _('In Progress')),
        ('completed', _('Completed')),
        ('cancelled', _('Cancelled')),
    ]

    sales_order = models.ForeignKey('Sales.SalesOrder', on_delete=models.CASCADE, related_name='manufacturing_orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Manufacturing Order for {self.sales_order}"

class MaterialRequisition(models.Model):
    manufacturing_order = models.ForeignKey(ManufacturingOrder, on_delete=models.CASCADE, related_name='material_requisitions')
    # Add other fields as needed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Material Requisition for {self.manufacturing_order}"

class BillOfMaterial(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class BOMItem(models.Model):
    bill_of_material = models.ForeignKey(BillOfMaterial, on_delete=models.CASCADE, related_name='bom_items')
    product = models.ForeignKey('Sales.Product', on_delete=models.CASCADE, related_name='bom_items')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product}"

    class Meta:
        verbose_name = _('BOM Item')
        verbose_name_plural = _('BOM Items')
