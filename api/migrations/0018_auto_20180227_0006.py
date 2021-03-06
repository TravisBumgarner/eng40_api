# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20180227_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.ManyToManyField(blank=True, to='api.Location'),
        ),
    ]
