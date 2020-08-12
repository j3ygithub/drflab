# Generated by Django 3.1 on 2020-08-12 09:36

import crm.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=crm.models.get_default_code, editable=False, max_length=100, verbose_name='Code')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Name')),
                ('tax_id', models.CharField(blank=True, max_length=25, verbose_name='Tax ID')),
                ('phone_number', models.CharField(blank=True, max_length=25, verbose_name='Phone Number')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Address')),
                ('registration_time', models.DateTimeField(blank=True, null=True, verbose_name='Registration Time')),
                ('expiration_time', models.DateTimeField(blank=True, null=True, verbose_name='Expiration Time')),
                ('remark', models.CharField(blank=True, max_length=400, verbose_name='Remark')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whose_person_parent', to='crm.person', verbose_name='Parent')),
                ('related_salesperson', models.ManyToManyField(blank=True, related_name='whose_person_related_salesperson', to='crm.Person', verbose_name='Related Salespersons')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
                'ordering': [django.db.models.functions.text.Concat('name', django.db.models.expressions.Value(' ('), 'code', django.db.models.expressions.Value(')'))],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=crm.models.get_default_code, editable=False, max_length=100, verbose_name='Code')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Name')),
                ('power_state', models.CharField(blank=True, max_length=25, verbose_name='Power State')),
                ('os', models.CharField(blank=True, max_length=50, verbose_name='OS')),
                ('cpu', models.IntegerField(blank=True, null=True, verbose_name='CPU')),
                ('ram', models.IntegerField(blank=True, null=True, verbose_name='RAM (GB)')),
                ('registration_time', models.DateTimeField(blank=True, null=True, verbose_name='Registration Time')),
                ('expiration_time', models.DateTimeField(blank=True, null=True, verbose_name='Expiration Time')),
                ('vmware_tool_state', models.CharField(blank=True, max_length=25, verbose_name='VMware Tool State')),
                ('remark', models.CharField(blank=True, max_length=400, verbose_name='Remark')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whose_device_customer', to='crm.person', verbose_name='Customer')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whose_device_parent', to='crm.device', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
                'ordering': [django.db.models.functions.text.Concat('name', django.db.models.expressions.Value(' ('), 'code', django.db.models.expressions.Value(')'))],
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['id'], name='crm_person_id_77f6da_idx'),
        ),
        migrations.AddIndex(
            model_name='device',
            index=models.Index(fields=['id'], name='crm_device_id_231208_idx'),
        ),
    ]
