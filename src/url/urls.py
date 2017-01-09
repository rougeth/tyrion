from django.conf.urls import include, url

from . import views
from .api import URLResource


urlpatterns = [
    url(r'api/url/', include(URLResource.urls())),
    url(r'(?P<short>\w*)/$', views.url_redirect, name='url_redirect'),
]
