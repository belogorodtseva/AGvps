# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-14 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_auto_20170808_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_en', models.CharField(max_length=3000)),
                ('block_ru', models.CharField(max_length=3000)),
                ('block_ua', models.CharField(max_length=3000)),
                ('number', models.IntegerField(default='1')),
            ],
        ),
        migrations.CreateModel(
            name='ContactLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(null=True, upload_to='')),
                ('link', models.CharField(max_length=300)),
                ('number', models.IntegerField(default='1')),
            ],
        ),
        migrations.RemoveField(
            model_name='arch_projects',
            name='mainimgchange',
        ),
        migrations.RemoveField(
            model_name='arch_projects',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='arch_projects',
            name='name_ua',
        ),
        migrations.RemoveField(
            model_name='design_projects',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='design_projects',
            name='name_ua',
        ),
    ]
