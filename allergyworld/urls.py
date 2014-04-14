from django.conf.urls import patterns, url, include
from allergyworld import views
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),                
    url(r'^$', views.search_formA),
    url(r'^v2/$', views.search_formB),
    url(r'^search/$',views.search),
    url(r'^signup/$',views.signup),
    url(r'^(?P<r_id>\d+)/$',views.details, name="details"),
)

