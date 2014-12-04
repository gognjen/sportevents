from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'invitations.views.home_page', name='home'),
    url(r'^invitations/test-sample/$', 'invitations.views.view_invitation', name='view_invitation'),
    url(r'^invitations/new$', 'invitations.views.new_invitation', name='new_invitation'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
