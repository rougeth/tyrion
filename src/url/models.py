from django.db import models

from pybaco import Baco


class URL(models.Model):
    url = models.URLField(max_length=512, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}:{}'.format(self.url, self.short)

    @property
    def short(self):
        return Baco.to_62(self.id)
