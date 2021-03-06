# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-16 01:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180215_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='category',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tool',
        ),
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='camera',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='exposure',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='external_src',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='local_src',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='link',
            name='image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Image'),
        ),
        migrations.AlterField(
            model_name='link',
            name='src',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Category'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='rating',
            field=models.CharField(blank=True, choices=[(b'novice', b'Novice'), (b'intermediate', b'Intermediate'), (b'advanced', b'Advanced'), (b'expert', b'Expert')], max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Tool',
        ),
    ]
