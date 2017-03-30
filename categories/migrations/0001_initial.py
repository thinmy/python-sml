# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category name')),
                ('active', models.BooleanField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Pending Approval')], default=2, verbose_name='Active')),
            ],
        ),
    ]
