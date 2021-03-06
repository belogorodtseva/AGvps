# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 20:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragraphs_arch_cd',
            name='language',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Architecture'),
        ),
        migrations.AddField(
            model_name='paragraphs_arch_cd',
            name='paragraph',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_arch_dd',
            name='language',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Architecture'),
        ),
        migrations.AddField(
            model_name='paragraphs_arch_dd',
            name='paragraph',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_arch_sd',
            name='language',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Architecture'),
        ),
        migrations.AddField(
            model_name='paragraphs_arch_sd',
            name='paragraph',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_as',
            name='language',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Architects_supervision'),
        ),
        migrations.AddField(
            model_name='paragraphs_as',
            name='paragraph',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_id',
            name='language',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Interior_design'),
        ),
        migrations.AddField(
            model_name='paragraphs_id',
            name='paragraph',
            field=models.CharField(default='some string', max_length=300),
        ),
        migrations.AddField(
            model_name='paragraphs_pd',
            name='language',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product_design'),
        ),
        migrations.AddField(
            model_name='paragraphs_pd',
            name='paragraph',
            field=models.CharField(default='some string', max_length=300),
        ),
    ]
