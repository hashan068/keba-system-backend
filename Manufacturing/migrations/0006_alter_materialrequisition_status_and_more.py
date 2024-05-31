# Generated by Django 5.0.6 on 2024-05-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manufacturing', '0005_alter_materialrequisition_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialrequisition',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('partialy_approved', 'Partially_Approved'), ('fulfilled', 'Fulfilled')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='materialrequisitionitem',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('partialy_approved', 'Partially_Approved'), ('fulfilled', 'Fulfilled')], default='pending', max_length=20),
        ),
    ]