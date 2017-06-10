# coding:utf-8
import xadmin
from .models import UserFav, UserAsk, UserMessage, UserComment, UserCourse


class UserFavAdmin(object):
    list_display = ('user', 'fav_type', 'add_time')
    list_filter = ('user', 'fav_type')
    search_fields = ('user', 'fav_type', 'fav_id')


class UserAskAdmin(object):
    list_display = ('user', 'mobile_phone', 'course', 'add_time')
    list_filter = ('user', 'mobile_phone', 'course')
    search_fields = ('user', 'mobile_phone', 'course')


class UserCourseAdmin(object):
    list_display = ('user', 'course', 'add_time')
    list_filter = ('user', 'course')
    search_fields = ('user', 'course')


class UserCommentAdmin(object):
    list_display = ('user', 'course', 'comment_content', 'add_time')
    list_filter = ('user', 'course')
    search_fields = ('user', 'course', 'comment_content')


class UserMessageAdmin(object):
    list_display = ('user', 'message', 'has_read', 'add_time')
    list_filter = ('user', 'has_read', 'message')
    search_fields = ('user', 'has_read', 'message')


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserComment, UserCommentAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
