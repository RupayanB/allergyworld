from django.conf.urls import patterns, url

from allergyworld import views

urlpatterns = patterns('',
                       
    url(r'^search_formA/$', views.search_formA),
    url(r'^search_formB/$', views.search_formB),
    url(r'^search/$',views.search),
    url(r'^(?P<r_id>\d+)/$',views.details, name="details"),
)

