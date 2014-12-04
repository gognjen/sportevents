from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'invitations.views.home_page', name='home'),
    url(r'^invitations/', include('invitations.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
