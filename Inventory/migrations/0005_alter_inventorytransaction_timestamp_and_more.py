# Generated by Django 5.0.4 on 2024-05-15 19:12

import Inventory.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0004_alter_inventorytransaction_options_and_more'),
        ('Manufacturing', '0008_remove_materialrequisition_component_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorytransaction',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='purchaserequisition',
            name='creator',
            field=models.ForeignKey(default=Inventory.models.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.CreateModel(
            name='MaterialRequisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('created', 'Created'), ('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('cancelled', 'Cancelled')], default='created', max_length=20)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(default=Inventory.models.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('manufacturing_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manufacturing.manufacturingorder')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='MaterialRequisitionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.component')),
                ('material_requisition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.materialrequisition')),
            ],
        ),
    ]
