# Generated by Django 5.0.1 on 2024-01-08 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestateapp', '0004_tenentreg_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenantRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('property_interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestateapp.propertydetail')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestateapp.tenentreg')),
            ],
        ),
    ]
