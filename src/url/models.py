from django.db import models

from pybaco import Baco


class URLManager(models.Manager):
    def get_queryset(self):
        qs = super(URLManager, self).get_queryset()
        return qs.annotate(clicks=models.Count('click'))


class URL(models.Model):
    url = models.URLField(max_length=512, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = URLManager()

    def __str__(self):  # pragma: no cover
        return self.url

    @property
    def short(self):
        return Baco.to_62(self.id)


class Click(models.Model):
    url = models.ForeignKey(URL)
    ip = models.GenericIPAddressField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # pragma: no cover
        return '{}:{}:{}'.format(self.url, self.ip, self.date)
