from restkiss.dj import DjangoResource
from restkiss.preparers import FieldsPreparer

from .models import Url


class UrlResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'url': 'url',
        'short': 'short'
    })

    def is_authenticated(self):
        return True

    def create(self):
        return Url.objects.create(
            url=self.data['url']
        )

    def list(self):
        return Url.objects.all()

    def detail(self, pk):
        return Url.objects.get(id=pk)

    def delete(self, pk):
        Url.objects.get(id=pk).delete()
