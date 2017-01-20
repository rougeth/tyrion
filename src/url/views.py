from django.http import HttpResponseRedirect
from django.views.defaults import page_not_found

from ipware.ip import get_real_ip

from pybaco import Baco, base62

from .models import URL, Click


def url_redirect(request, short):
    id = Baco.to_dec(short, base62)

    try:
        url = URL.objects.get(id=id)
    except URL.DoesNotExist as e:
        return page_not_found(request, e, 'url/404.html')

    # Get a more precise request datetime
    ip = get_real_ip(request) or '0.0.0.0'
    Click.objects.create(url=url, ip=ip)

    return HttpResponseRedirect(url.url)
