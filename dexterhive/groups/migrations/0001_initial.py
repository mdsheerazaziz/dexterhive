# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-30 07:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('modelbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.ModelBase')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('avatar', models.URLField(null=True)),
                ('name', models.CharField(default='', max_length=127)),
                ('description', models.TextField(null=True)),
                ('type', models.CharField(default='', max_length=63)),
                ('visibility', models.CharField(default='Public', max_length=15)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.Groups')),
            ],
            bases=('core.modelbase',),
        ),
    ]