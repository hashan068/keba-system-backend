# Generated by Django 5.0.4 on 2024-05-25 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manufacturing', '0003_alter_materialrequisition_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialrequisitionitem',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('fulfilled', 'Fulfilled')], default='pending', max_length=20),
        ),
    ]