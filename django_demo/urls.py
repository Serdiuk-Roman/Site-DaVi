from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lit/', include('coder_page.urls')),
    url(r'^demo_gallery/', include('demo_gallery.urls')),
    url(r'^nodeads/', include('nodeads.urls')),
    url(r'^', include('first_page.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
