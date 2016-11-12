from django.db import models


class Url(models.Model):
    url = models.URLField(max_length=512)
    hash = models.CharField(max_length=256, unique=True, blank=True)

    def __str__(self):
        return '{}:{}'.format(self.url, self.hash)
