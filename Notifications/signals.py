# notifications/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from your_app.models import YourModel

@receiver(post_save, sender=YourModel)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.user,
            message=f"A new {instance.__class__.__name__} has been created."
        )