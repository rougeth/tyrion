from django.http import HttpResponse, HttpResponseRedirect

from pybaco import Baco, base62

from .models import URL


def url_redirect(request, short):
    id = Baco.to_dec(short, base62)

    try:
        url = URL.objects.get(id=id)
    except URL.DoesNotExist:
        return HttpResponse('not found', status=404)

    return HttpResponseRedirect(url.url)
