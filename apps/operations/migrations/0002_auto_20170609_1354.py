# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-09 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('operations', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.User', verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='userfav',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User', verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='\u8bfe\u7a0b\u540d\u79f0'),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User', verbose_name='\u7528\u6237\u540d\u79f0'),
        ),
        migrations.AddField(
            model_name='usercomment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='\u8bfe\u7a0b'),
        ),
        migrations.AddField(
            model_name='usercomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User', verbose_name='\u7528\u6237'),
        ),
    ]
