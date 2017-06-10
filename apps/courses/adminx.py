# coding: utf-8
import xadmin

from .models import Course, Chapter, Video, CourseResource


class CourseAdmin(object):
    list_display = ('title', 'degree', 'fav_nums', 'student_nums', 'add_time')
    search_fields = ('title', 'desc', 'detail')
    list_filter = ('degree', 'fav_nums')


class ChapterAdmin(object):
    list_display = ('course', 'name', 'add_time')
    search_fields = ('course', 'name')
    list_filter = ('course',)


class VideoAdmin(object):
    list_display = ('name', 'chapter', 'url', 'add_time')
    search_fields = ('name', 'chapter')
    list_filter = ('name', 'chapter')


class CourseResourceAdmin(object):
    list_display = ('course', 'name', 'add_time')
    search_fields = ('course', 'name')
    list_filter = ('course', 'name')


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
