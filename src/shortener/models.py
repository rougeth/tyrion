import random
from django.db import models


class Url(models.Model):
    url = models.URLField(max_length=512, unique=True)
    # need to check if 256 is the best length for the short url
    short = models.CharField(max_length=256, unique=True, blank=True)

    def __str__(self):
        return '{}:{}'.format(self.url, self.short)

    # Just for test. Need to be modified.
    def _generate_hash(self):
        h = 0
        for c in self.url:
            h += ord(c) * ord(random.choice(self.url))
        return h

    def save(self, *args, **kwargs):
        if not self.short:
            self.short = self._generate_hash()
        super(Url, self).save(*args, **kwargs)
