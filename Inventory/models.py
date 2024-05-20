from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model

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
    unit_of_measure = models.CharField(max_length=20, default='pcs')
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name

class PurchaseRequisition(models.Model):
    CREATED = 'created'
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (CREATED, _('Created')),
        (PENDING, _('Pending')),
        (APPROVED, _('Approved')),
        (REJECTED, _('Rejected')),
        (CANCELLED, _('Cancelled'))
    ]

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=CREATED
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Purchase Requisition #{self.id} - {self.component} - {self.quantity} units"

class MaterialRequisition(models.Model):
    CREATED = 'created'
    PENDING = 'pending'
    APPROVED = 'approved'
    FULFILLED = 'fulfilled'
    REJECTED = 'rejected'
    CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (CREATED, _('Created')),
        (PENDING, _('Pending')),
        (APPROVED, _('Approved')),
        (FULFILLED, _('Fulfilled')),
        (REJECTED, _('Rejected')),
        (CANCELLED, _('Cancelled'))
    ]

    manufacturing_order = models.ForeignKey('Manufacturing.ManufacturingOrder', on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=CREATED
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Material Requisition #{self.id} - {self.manufacturing_order}"

class MaterialRequisitionItem(models.Model):
    material_requisition = models.ForeignKey('MaterialRequisition', on_delete=models.CASCADE)
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} units of {self.component} for {self.material_requisition}"

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
    material_requisition_item = models.ForeignKey('MaterialRequisitionItem', on_delete=models.CASCADE)
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Consumption of {self.quantity} {self.component} at {self.timestamp}"
