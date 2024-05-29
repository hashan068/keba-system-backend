# Inventory app models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from Notifications.models import Notification

User = get_user_model()

def get_default_user():
    return User.objects.filter(is_superuser=True).first()

superuser = get_default_user()
superuser_pk = superuser.pk if superuser else 1

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default=None)
    address = models.TextField(null=True, blank=True)
    website = models.URLField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Suppliers'

class Component(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=0)
    reorder_quantity = models.PositiveIntegerField(default=0)
    order_quantity = models.PositiveIntegerField(default=0)
    unit_of_measure = models.CharField(max_length=20, default='pcs')
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name

    def check_inventory(self):
        if self.quantity < self.reorder_level and self.order_quantity == 0:
            self.notify_low_inventory()

    def notify_low_inventory(self):
        user = get_default_user()
        Notification.objects.create(
            user=user,
            message=f"Inventory level for {self.name} is below the reorder level."
    )


class PurchaseRequisition(models.Model):
    # Define choices for status
    STATUS_CHOICES = [
        ('pending', _('Pending')),
        ('approved', _('Approved')),
        ('rejected', _('Rejected')),
        ('cancelled', _('Cancelled')),
        ('fulfilled', _('Fulfilled')),
    ]

    # Define choices for priority
    PRIORITY_CHOICES = [
        ('high', _('High')),
        ('medium', _('Medium')),
        ('low', _('Low')),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expected_delivery_date = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='high')

class PurchaseOrder(models.Model):
    CREATED = 'created'
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED ='rejected'
    CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (CREATED, _('Created')),
        (PENDING, _('Pending')),
        (APPROVED, _('Approved')),
        (REJECTED, _('Rejected')),
        (CANCELLED, _('Cancelled'))
    ]

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, default=None)
    
    purchase_requisition = models.ForeignKey('PurchaseRequisition', on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, blank=True)
    purchase_manager_approval = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=CREATED
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Purchase Order #{self.id} - {self.purchase_requisition.component} - {self.purchase_requisition.quantity} units"

class ReplenishTransaction(models.Model):  # Corrected class name
    purchase_requisition = models.ForeignKey('PurchaseRequisition', on_delete=models.CASCADE)
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Replenish of {self.quantity} {self.component} at {self.timestamp}"

class ConsumptionTransaction(models.Model):
    material_requisition_item = models.ForeignKey('Manufacturing.MaterialRequisitionItem', on_delete=models.CASCADE)
    component_id = models.ForeignKey('Inventory.Component', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)


    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Consumption of {self.quantity} {self.component_id.name} at {self.timestamp}"
