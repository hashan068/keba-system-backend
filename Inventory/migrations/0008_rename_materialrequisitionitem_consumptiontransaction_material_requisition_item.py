# Generated by Django 5.0.4 on 2024-05-20 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0007_remove_consumptiontransaction_materialrequisition_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consumptiontransaction',
            old_name='MaterialRequisitionItem',
            new_name='material_requisition_item',
        ),
    ]
