from pybaco import Baco, base62
from restkiss.dj import DjangoResource
from restkiss.preparers import FieldsPreparer

from .models import Url


class UrlResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'url': 'url',
        'short': 'short',
        'created': 'created',
        'updated': 'updated',
    })

    def is_authenticated(self):
        return True

    def create(self):
        return Url.objects.create(url=self.data['url'])

    def list(self):
        return Url.objects.all()

    def detail(self, pk):
        id = Baco.to_dec(pk, base62)
        return Url.objects.get(id=id)

    def delete(self, pk):
        id = Baco.to_dec(pk, base62)
        Url.objects.get(id=id).delete()
