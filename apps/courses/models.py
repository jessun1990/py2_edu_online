# coding: utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from organizations.models import Organization, Teacher
# Create your models here.


class Course(models.Model):
    degree_choices = (
        (1, u'初级'),
        (2, u'中级'),
        (3, u'高级'),
    )
    title = models.CharField(verbose_name=u'课程名称', max_length=50)
    desc = models.CharField(verbose_name=u'课程简介', max_length=300)
    degree = models.IntegerField(choices=degree_choices, verbose_name=u'课程的难度')
    learn_times = models.IntegerField(verbose_name=u'学习时长（分钟数）')
    fav_nums = models.IntegerField(verbose_name=u'收藏数', default=0)
    student_nums = models.IntegerField(verbose_name=u'学习人数', default=0)
    click_nums = models.IntegerField(verbose_name=u'点击数', default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    detail = models.TextField(verbose_name=u'课程详情')
    cover_image = models.ImageField(upload_to='upload/courses/images/%Y/%m', verbose_name=u'封面图', max_length=300)
    course_org = models.ForeignKey(Organization, verbose_name=u'课程机构')
    teacher = models.ForeignKey(Teacher, verbose_name=u'主讲老师')
    category = models.CharField(verbose_name=u'课程类别', max_length=20, default="")
    must_know = models.CharField(verbose_name=u"课程须知", max_length=40, default="")
    teacher_tells_your = models.CharField(verbose_name=u"老师告诉你能学到什么", max_length=40, default="")
    announcement = models.CharField(verbose_name=u"课程公告", max_length=40, default="")

    class Meta:
        verbose_name = u'课程信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

    def get_video_nums(self):
        return Video.objects.filter(chapter__course_id=self.id).count()


class Chapter(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'所属课程')
    name = models.CharField(verbose_name=u'章节名称', max_length=50)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u'章节信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    chapter = models.ForeignKey(Chapter, verbose_name=u'所属章节')
    name = models.CharField(verbose_name=u'视频名称', max_length=10)
    url = models.URLField(verbose_name=u'视频地址', max_length=300, default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u'视频信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'所属课程')
    name = models.CharField(verbose_name=u'资源名称', max_length=20)
    file = models.FileField(verbose_name=u'资源文件', upload_to='upload/courses/resources/%Y/%m', max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name

