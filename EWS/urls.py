from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', DefaultView.as_view(), name='default'),
    url(r'^drought', DroughtView.as_view(), name='drought_home'),
    url(r'^flood', FloodView.as_view(), name='flood_home'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
            {'template_name': 'login.html'}, name='auth_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name='auth_logout'),
    url(r'^admin/', include(admin.site.urls)),
)
