from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', 'demo_gallery.views.home', name='home'),
    url(r'^contact/$', 'demo_gallery.views.contact', name='contact'),
    url(r'^item/(?P<item_id>[0-9]+)/$', 'demo_gallery.views.show_item', name='item'),
    url(r'^list/$', 'demo_gallery.views.list', name='list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
