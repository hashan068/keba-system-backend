# Generated by Django 5.0.4 on 2024-05-19 10:04

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0005_alter_inventorytransaction_timestamp_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialrequisition',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('pending', 'Pending'), ('approved', 'Approved'), ('fulfilled', 'Fulfilled'), ('rejected', 'Rejected'), ('cancelled', 'Cancelled')], default='created', max_length=20),
        ),
        migrations.CreateModel(
            name='ConsumptionTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('MaterialRequisition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.materialrequisition')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.component')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='ReplenishTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.component')),
                ('purchase_requisition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.purchaserequisition')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.DeleteModel(
            name='InventoryTransaction',
        ),
    ]
