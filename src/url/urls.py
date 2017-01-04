from django.conf.urls import include, url

from .api import URLResource


urlpatterns = [
    url(r'api/url/', include(URLResource.urls())),
]
