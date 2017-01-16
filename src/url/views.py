from django.http import HttpResponseRedirect
from django.views.defaults import page_not_found

from pybaco import Baco, base62

from .models import URL


def url_redirect(request, short):
    id = Baco.to_dec(short, base62)

    try:
        url = URL.objects.get(id=id)
    except URL.DoesNotExist as e:
        return page_not_found(request, e, 'url/404.html')

    return HttpResponseRedirect(url.url)
