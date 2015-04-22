from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', DefaultView.as_view(), name='default'),
    url(r'^home', Home.as_view(), name='home'),
    url(r'^drought', DroughtView.as_view(), name='drought_home'),
    url(r'^flood', FloodView.as_view(), name='flood_home'),
    url(r'^nzoia', Nzoia.as_view(), name='nzoia'),
    url(r'^kwale', Kwale.as_view(), name='kwale'),
    url(r'^turkana', Turkana.as_view(), name='turkana'),
    url(r'^case-studies/(?P<tab>\w+)/$', CaseStudies.as_view(), name='casestudies'),
    url(r'^mafuriko', Mafuriko.as_view(), name='mafuriko'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
            {'template_name': 'login.html'}, name='auth_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name='auth_logout'),
    url(r'^admin/', include(admin.site.urls)),
)
