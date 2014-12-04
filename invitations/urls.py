from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^(\d+)/$', 'invitations.views.view_invitation', name='view_invitation'),
    url(r'^(\d+)/add_message$', 'invitations.views.add_message', name='add_message'),
    url(r'^new$', 'invitations.views.new_invitation', name='new_invitation'),
)
