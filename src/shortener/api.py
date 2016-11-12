from restkiss.dj import DjangoResource
from restkiss.preparers import FieldsPreparer

from .models import Url


class UrlResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'url': 'url'
    })

    def is_authenticated(self):
        return True

    def create(self):
        return Url.objects.create(
            url=self.data['url']
        )
