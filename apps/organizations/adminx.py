# coding:utf-8
import xadmin
from .models import CityDict, Organization, Teacher


class CityDictAdmin(object):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class OrganizationAdmin(object):
    list_display = ('name', 'org_type', 'fav_nums', 'city', 'add_time')
    search_fields = ('name', 'fav_nums', 'click_nums')
    list_filter = ('city', 'org_type', 'fav_nums', 'click_nums')


class TeacherAdmin(object):
    list_display = ('name', 'work_years', 'work_position', 'age', 'add_time')
    search_fields = ('name', 'work_company', 'work_years')
    list_filter = ('fav_nums', 'age', 'work_years')


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(Organization, OrganizationAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
