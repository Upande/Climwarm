from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import DefaultView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', DefaultView.as_view(), name='default'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login', 
        {'template_name': 'login.html'}, name='auth_login'),
	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name='auth_logout'),
    url(r'^admin/', include(admin.site.urls)),
)
