# Generated by Django 5.0.6 on 2024-06-12 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manufacturing', '0003_manufacturingorder_end_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manufacturingorder',
            old_name='product_id',
            new_name='product',
        ),
    ]
