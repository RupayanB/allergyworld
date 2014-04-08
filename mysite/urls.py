from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', lambda r : HttpResponseRedirect('allergyworld/')),
    url(r'^allergyworld/', include('allergyworld.urls', namespace="allergyworld")),
)
