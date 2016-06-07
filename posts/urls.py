from django.conf.urls import url
from django.contrib import admin

from views import (

	post_create,
	post_update,
	post_detail,
	post_list,
	post_delete,



)
urlpatterns = [
   
    url(r'^create/$', post_create),
    url(r'^update/$', post_update),
    url(r'^(?P<id>\d+)/$', post_detail),
    url(r'^$', post_list),
    url(r'^delete$', post_delete),
]