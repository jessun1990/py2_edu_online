# coding: utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    gender_choices = (
        (1, u'男'),
        (2, u'女')
    )
    nickname = models.CharField(verbose_name=u'昵称', max_length=20, default="")
    age = models.IntegerField(verbose_name=u"年龄", blank=True, null=True)
    gender = models.IntegerField(choices=gender_choices, verbose_name=u'性别', default=1)
    address = models.CharField(verbose_name=u'地址', max_length=200, default="")
    mobile_phone = models.CharField(verbose_name=u'手机号', max_length=11, default="")
    avatar = models.ImageField(verbose_name=u'头像', max_length=200, upload_to='upload/users/avatars/%Y/%m', default='upload/users/avatars/default.png')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name
