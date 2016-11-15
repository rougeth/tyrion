import random
from django.db import models


class Url(models.Model):
    url = models.URLField(max_length=512)
    hash = models.CharField(max_length=256, unique=True, blank=True)

    def __str__(self):
        return '{}:{}'.format(self.url, self.hash)

    # Just for test. Need to be modified.
    def _generate_hash(self):
        h = 0
        for c in self.url:
            h += ord(c) * ord(random.choice(self.url))
        return h

    def save(self, *args, **kwargs):
        self.hash = self._generate_hash()
        super(Url, self).save(*args, **kwargs)
