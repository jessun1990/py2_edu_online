# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-12 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20170612_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='announcement',
            field=models.CharField(default='', max_length=40, verbose_name='\u8bfe\u7a0b\u516c\u544a'),
        ),
        migrations.AlterField(
            model_name='course',
            name='must_know',
            field=models.CharField(default='', max_length=40, verbose_name='\u8bfe\u7a0b\u987b\u77e5'),
        ),
    ]