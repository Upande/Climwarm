from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import DefaultView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', DefaultView.as_view(), name='default'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
