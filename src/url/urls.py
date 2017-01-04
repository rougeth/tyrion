from django.conf.urls import include, url

from .api import UrlResource


urlpatterns = [
    url(r'api/url/', include(UrlResource.urls())),
]
