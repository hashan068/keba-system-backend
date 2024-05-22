# Generated by Django 5.0.4 on 2024-05-22 14:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_component_reorder_quantity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchaserequisition',
            options={},
        ),
        migrations.RemoveField(
            model_name='purchaserequisition',
            name='creator',
        ),
        migrations.AddField(
            model_name='purchaserequisition',
            name='expected_delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaserequisition',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='high', max_length=20),
        ),
        migrations.AddField(
            model_name='purchaserequisition',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='purchaserequisition',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('cancelled', 'Cancelled'), ('partially_fulfilled', 'Partially Fulfilled'), ('fulfilled', 'Fulfilled'), ('closed', 'Closed')], default='created', max_length=20),
        ),
    ]