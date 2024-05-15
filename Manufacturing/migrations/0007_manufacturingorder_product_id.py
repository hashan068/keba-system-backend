# Generated by Django 5.0.4 on 2024-05-13 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manufacturing', '0006_alter_bomitem_options_and_more'),
        ('Sales', '0007_product_bom'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturingorder',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manufacturing_orders', to='Sales.product'),
        ),
    ]