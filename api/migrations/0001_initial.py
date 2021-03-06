# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-09 00:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('external_src', models.URLField(blank=True)),
                ('local_src', models.ImageField(blank=True, upload_to=b'')),
                ('camera', models.CharField(blank=True, max_length=200)),
                ('exposure', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('src', models.URLField(blank=True)),
                ('image', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('category', models.ManyToManyField(blank=True, to='api.Category')),
                ('image', models.ManyToManyField(blank=True, to='api.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rating', models.CharField(choices=[(b'novice', b'Novice'), (b'intermediate', b'Intermediate'), (b'advanced', b'Advanced'), (b'expert', b'Expert')], max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('src', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='skill',
            field=models.ManyToManyField(blank=True, to='api.Skill'),
        ),
        migrations.AddField(
            model_name='project',
            name='tool',
            field=models.ManyToManyField(blank=True, to='api.Tool'),
        ),
        migrations.AddField(
            model_name='project',
            name='video',
            field=models.ManyToManyField(blank=True, to='api.Video'),
        ),
    ]
