from django.conf.urls import patterns, url

from allergyworld import views

urlpatterns = patterns('',
                       
    url(r'^search_form/$', views.search_form),
    url(r'^search/$',views.search),
    url(r'^(?P<r_id>\d+)/$',views.details, name="details"),
)

