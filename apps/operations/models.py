# coding: utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from users.models import User
from courses.models import Course

# Create your models here.


class UserFav(models.Model):
    fav_type_choices = (
        (1, u'课程'),
        (2, u'讲师'),
        (3, u'机构'),
    )

    user = models.ForeignKey(User, verbose_name=u'用户')
    fav_type = models.IntegerField(verbose_name=u'收藏类型', choices=fav_type_choices)
    fav_id = models.IntegerField(verbose_name=u'收藏ID')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'收藏时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name


class UserAsk(models.Model):
    user = models.CharField(max_length=20, verbose_name=u'用户名称')
    mobile_phone = models.CharField(verbose_name=u'手机号', max_length=11, default="")
    course = models.CharField(verbose_name=u'课程名称', max_length=20)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'收藏时间')

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户名称')
    course = models.ForeignKey(Course, verbose_name=u'课程名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户课程'
        verbose_name_plural = verbose_name


class UserComment(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    comment_content = models.CharField(verbose_name=u'评论内容', max_length=300)

    class Meta:
        verbose_name = u'用户评论'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户', default=0)
    message = models.CharField(verbose_name=u'消息内容', max_length=300)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'消息内容')
    has_read = models.BooleanField(verbose_name=u'是否已读', default=False)

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name
