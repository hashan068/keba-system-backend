# Generated by Django 5.0.3 on 2024-03-30 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Sales', '0002_remove_product_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillOfMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BOMItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('bill_of_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bom_items', to='Manufacturing.billofmaterial')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bom_items', to='Sales.product')),
            ],
            options={
                'verbose_name': 'BOM Item',
                'verbose_name_plural': 'BOM Items',
            },
        ),
        migrations.CreateModel(
            name='ManufacturingOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sales_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manufacturing_orders', to='Sales.salesorder')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialRequisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('manufacturing_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_requisitions', to='Manufacturing.manufacturingorder')),
            ],
        ),
    ]
