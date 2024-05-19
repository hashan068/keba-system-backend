# Generated by Django 5.0.4 on 2024-05-15 12:32

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_alter_supplier_options_supplier_address_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventorytransaction',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='purchaseorder',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='purchaserequisition',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='contact_information',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='lead_time',
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='creator',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('cancelled', 'Cancelled')], default='created', max_length=20),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Inventory.supplier'),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='purchaserequisition',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaserequisition',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaserequisition',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='purchaserequisition',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventorytransaction',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='inventorytransaction',
            name='transaction_type',
            field=models.CharField(choices=[('replenish', 'Replenish'), ('consumption', 'Consumption'), ('scrapping', 'Scrapping')], default='replenish', max_length=20),
        ),
        migrations.AlterField(
            model_name='purchaserequisition',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('cancelled', 'Cancelled')], default='created', max_length=20),
        ),
    ]