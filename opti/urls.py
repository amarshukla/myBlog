from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    url(r'^$', views.login_user),
    url(r'^auth/$', views.auth_view),
    url(r'^login/$', views.login_user),
    url(r'^invalid/$', views.invalidLogin),
    url(r'^loggedin/$', views.loggedin),
    url(r'^logout/$', views.logout),
    url(r'^registera/$', views.registerUser),
    url(r'^index/$', views.list_dataset),
    url(r'^registerSuccess/$', views.registerSuccess),
    #url(r'^registerUser/$', views.registerUser),

)