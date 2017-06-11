# coding: utf-8
from django.conf.urls import url

from .views import OrgListView, UserAskView, OrgHomeView, OrgHomeCourseView, OrgHomeTeacherView, OrgHomeDescView


urlpatterns = [
    url(r'^list/$', OrgListView.as_view(), name='org_list'),
    url(r'^add_ask/$', UserAskView.as_view(), name='add_ask'),
    url(r'^add_ask/$', UserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_homepage'),
    url(r'^course/(?P<org_id>\d+)/$', OrgHomeCourseView.as_view(), name='org_course'),
    url(r'^desc/(?P<org_id>\d+)/$', OrgHomeDescView.as_view(), name='org_desc'),
    url(r'^teachers/(?P<org_id>\d+)/$', OrgHomeTeacherView.as_view(), name='org_teachers'),
]
