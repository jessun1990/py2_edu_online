# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-12 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='must_know',
            field=models.CharField(default='', max_length=30, verbose_name='\u8bfe\u7a0b\u987b\u77e5'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_tells_your',
            field=models.CharField(default='', max_length=40, verbose_name='\u8001\u5e08\u544a\u8bc9\u4f60\u80fd\u5b66\u5230\u4ec0\u4e48'),
        ),
    ]
