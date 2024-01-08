# Generated by Django 5.0.1 on 2024-01-08 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestateapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='propertydetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=60)),
                ('address', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('features', models.TextField()),
                ('property_type', models.CharField(choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')], max_length=6)),
                ('rent_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=False)),
            ],
        ),
    ]
