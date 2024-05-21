# Manufacturing app models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from Inventory.models import Component
from Sales.models import SalesOrderItem, Product
from django.utils import timezone
from django.contrib.auth import get_user_model


class ManufacturingOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', _('Pending')),
        ('in_progress', _('In Progress')),
        ('completed', _('Completed')),
        ('cancelled', _('Cancelled')),
    ]

    sales_order_item = models.ForeignKey(SalesOrderItem, on_delete=models.CASCADE, related_name='manufacturing_orders', null=True, blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='manufacturing_orders', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    bom = models.ForeignKey('BillOfMaterial', on_delete=models.CASCADE, related_name='manufacturing_orders', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        if self.sales_order_item:
            return f"Quotation #{self.pk}"
        else:
            return "Manufacturing Order with no associated Sales Order Item"


class MaterialRequisition(models.Model):
    STATUS_CHOICES = [
        ('pending', _('Pending')),
        ('approved', _('Approved')),
        ('rejected', _('Rejected')),
        ('fulfilled', _('Fulfilled')),
    ]

    manufacturing_order = models.ForeignKey(ManufacturingOrder, on_delete=models.CASCADE, related_name='material_requisitions')
    bom = models.ForeignKey('BillOfMaterial', on_delete=models.CASCADE, related_name='material_requisitions', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Material Requisition for {self.manufacturing_order}"


class MaterialRequisitionItem(models.Model):
    material_requisition = models.ForeignKey(MaterialRequisition, on_delete=models.CASCADE, related_name='items')
    component = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='material_requisition_items')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.component} for Material Requisition {self.material_requisition}"


class BillOfMaterial(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bill_of_material', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BOMItem(models.Model):
    bill_of_material = models.ForeignKey(BillOfMaterial, on_delete=models.CASCADE, related_name='bom_items')
    component = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='bom_items', null=True, default=1, blank=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.component}"

    class Meta:
        verbose_name = _('BOM Item')
