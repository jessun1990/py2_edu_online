# coding:utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class EmailVerifyRecord(models.Model):
    code_type_choices = (
            (1, u'激活邮箱'),
            (2, u'忘记密码')
        )
    code = models.CharField(verbose_name=u'激活码', max_length=20)
    email = models.EmailField(verbose_name=u'邮箱', max_length=25)
    code_type = models.IntegerField(choices=code_type_choices, verbose_name=u'验证类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    index = models.IntegerField(default=100, verbose_name=u'顺序')
    title = models.CharField(verbose_name=u'标题', max_length=100)
    url = models.URLField(verbose_name=u'跳转地址', max_length=200)
    image = models.ImageField(upload_to='upload/global/images/%Y/%m', verbose_name=u'封面图', max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name
