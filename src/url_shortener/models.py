from django.db import models
from django.utils import timezone

class Url(models.Model):
    url = models.CharField(max_length=500)
    short_url = models.CharField(max_length=500)
