from django.conf.urls import patterns, include, url
from django.contrib import admin
from api import WhateverResource
from whatever import views

whatever_resource = WhateverResource()
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(whatever_resource.urls)),
    url(r'^$', 'whatever.views.whatever'),
    url(r'^add/$', 'whatever.views.add'),
)
