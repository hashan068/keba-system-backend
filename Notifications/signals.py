# notifications/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from Inventory.models import Component, PurchaseOrder

# @receiver(post_save, sender=YourModel)
# def create_notification(sender, instance, created, **kwargs):
#     if created:
#         Notification.objects.create(
#             user=instance.user,
#             message=f"A new {instance.__class__.__name__} has been created."
#         )


@receiver(post_save, sender=Component)
def notify_low_inventory(sender, instance, **kwargs):
    instance.check_inventory()

@receiver(post_save, sender=PurchaseOrder)
def notify_purchase_order_approved(sender, instance, created, **kwargs):
    if created and instance.status == 'approved':
        Notification.objects.create(
            user=instance.creator,
            message=f"Purchase Order #{instance.id} has been approved."
        )
