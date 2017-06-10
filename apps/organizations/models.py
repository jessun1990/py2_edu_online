# coding: utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
# Create your models here.


class CityDict(models.Model):
    name = models.CharField(verbose_name=u'城市名称', max_length=12)
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'城市信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Organization(models.Model):
    type_choices = (
        ("pxjg", u'培训机构'),
        ("gx", u'高校'),
        ("gr", u'个人'),
    )
    name = models.CharField(verbose_name=u'机构名称', max_length=50)
    cover_image = models.ImageField(verbose_name=u'机构封面图', max_length=200, upload_to='upload/organizations/images/%Y/%m')
    fav_nums = models.IntegerField(verbose_name=u'收藏数', default=0)
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)
    desc = models.TextField(verbose_name=u'机构介绍')
    org_type = models.CharField(verbose_name=u'机构类别', choices=type_choices, default="", max_length=5)
    city = models.ForeignKey(CityDict, verbose_name=u'所在城市')
    click_nums = models.IntegerField(verbose_name=u'点击数', default=0)
    address = models.CharField(verbose_name=u'机构地址', max_length=100, default="")
    student_nums = models.IntegerField(verbose_name=u'学生人数', default=0)
    course_nums = models.IntegerField(verbose_name=u'课程数', default=0)

    class Meta:
        verbose_name = u'授课机构'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_course_nums(self):
        return self.course_set.count()


class Teacher(models.Model):
    name = models.CharField(verbose_name=u'姓名', max_length=20)
    work_years = models.IntegerField(verbose_name=u'工作年限')
    work_company = models.CharField(verbose_name=u'就职公司', max_length=30)
    work_position = models.CharField(verbose_name=u'工作职位', max_length=10)
    feature = models.CharField(verbose_name=u'教学特点', max_length=50)
    age = models.IntegerField(verbose_name=u'年龄')
    fav_nums = models.IntegerField(verbose_name=u'收藏数', default=0)
    avatar = models.ImageField(verbose_name=u'头像', upload_to='upload/teachers/avatars/%Y/%m', default='upload/teachers/avatars/default.png')
    add_time = models.DateTimeField(verbose_name=u'添加时间', default=datetime.now)
    org = models.ForeignKey(Organization, verbose_name=u'所属机构', default="")

    class Meta:
        verbose_name = u'授课教师'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
