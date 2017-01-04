from pybaco import Baco, base62
from restkiss.dj import DjangoResource
from restkiss.preparers import FieldsPreparer

from .models import URL


class URLResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'url': 'url',
        'short': 'short',
        'created': 'created',
        'updated': 'updated',
    })

    def is_authenticated(self):
        return True

    def create(self):
        return URL.objects.create(url=self.data['url'])

    def list(self):
        return URL.objects.all()

    def detail(self, pk):
        id = Baco.to_dec(pk, base62)
        return URL.objects.get(id=id)

    def delete(self, pk):
        id = Baco.to_dec(pk, base62)
        URL.objects.get(id=id).delete()
