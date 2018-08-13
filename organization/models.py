import datetime

from django.db import models
from django.utils import timezone

class Organization(models.Model):
    """
    Organization model
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField('created at', default=timezone.now())
    updated_at = models.DateTimeField('updated at', default=timezone.now())

    def __str__(self):
        return self.name
