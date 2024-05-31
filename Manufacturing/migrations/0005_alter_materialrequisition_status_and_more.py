# Generated by Django 5.0.6 on 2024-05-31 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manufacturing', '0004_materialrequisitionitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialrequisition',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('partialy_fulfilled', 'Partially Fulfilled'), ('fulfilled', 'Fulfilled')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='materialrequisitionitem',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('partialy_fulfilled', 'Partially Fulfilled'), ('fulfilled', 'Fulfilled')], default='pending', max_length=20),
        ),
    ]