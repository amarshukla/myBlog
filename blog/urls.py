from django.conf.urls import patterns, include, url
from . import views
from .forms import PostForm

urlpatterns = patterns('',
	url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
)