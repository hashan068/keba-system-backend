from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MaterialRequisitionItem

@receiver(post_save, sender=MaterialRequisitionItem)
def update_material_requisition_status(sender, instance, **kwargs):
    instance.material_requisition.update_status()

