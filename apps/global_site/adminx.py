# coding: utf-8
import xadmin
from xadmin.views import BaseAdminView, CommAdminView

from .models import EmailVerifyRecord, Banner


class GlobalSetting(object):
    site_title = 'edu_online'
    site_footer = 'edu_online'
    menu_style = 'accordion'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class EmailVerifyRecordAdmin(object):
    search_fields = ('email', 'code_type')
    list_display = ('email', 'code', 'code_type', 'add_time')
    list_filter = ('code_type',)
    ordering = ('add_time',)


class BannerAdmin(object):
    search_fields = ('index', 'title', 'url')
    list_display = ('index', 'title', 'url', 'add_time')
    list_filter = ('index', 'title')
    ordering = ('add_time',)


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(CommAdminView, GlobalSetting)
xadmin.site.register(BaseAdminView, BaseSetting)
