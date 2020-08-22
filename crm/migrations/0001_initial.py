# Generated by Django 3.1 on 2020-08-22 06:04

import crm.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=crm.models.get_default_uuid, editable=False, max_length=63, verbose_name='UUID')),
                ('name', models.CharField(blank=True, max_length=63, verbose_name='Name')),
                ('phone_number', models.CharField(blank=True, max_length=63, verbose_name='Phone Number')),
                ('remark', models.CharField(blank=True, max_length=255, verbose_name='Remark')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=crm.models.get_default_uuid, editable=False, max_length=63, verbose_name='UUID')),
                ('name', models.CharField(blank=True, max_length=63, verbose_name='Name')),
                ('os', models.CharField(blank=True, max_length=50, verbose_name='OS')),
                ('cpu', models.IntegerField(blank=True, null=True, verbose_name='CPU')),
                ('ram', models.IntegerField(blank=True, null=True, verbose_name='RAM (GB)')),
                ('remark', models.CharField(blank=True, max_length=400, verbose_name='Remark')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whose_device_customer', to='crm.person', verbose_name='Customer')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
                'ordering': ['id'],
            },
        ),
    ]
