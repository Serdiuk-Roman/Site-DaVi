from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.home, name='gallery'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^item/(?P<item_id>[0-9]+)/$', views.show_item, name='item'),
    url(r'^list/$', views.list, name='list'),
]
