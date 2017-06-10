# coding: utf-8
"""py2_edu_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
# from django.contrib import admin
import xadmin

from py2_edu_online.settings import MEDIA_ROOT
from users.views import LoginView, LogoutView, RegisterView, ActiveUserView, ForgetPwdView, ResetPwdView, ModifyPwdView

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$|^index/', include('global_site.urls')),

    #upload files
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # user
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='active_user'),
    url(r'^forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<reset_code>.*)/$', ResetPwdView.as_view(), name='reset_pwd'),
    url(r'^modify/', ModifyPwdView.as_view(), name='modify_pwd'),

    #org
    url(r'^org/', include('organizations.urls', namespace='org')),

]
