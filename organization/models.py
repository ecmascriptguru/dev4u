import datetime

from django.db import models
from django.utils import timezone

class Organization(models.Model):
    """
    Organization model
    """
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('created at')
    updated_at = models.DateTimeField('updated at')

    def __str__(self):
        return "<Organization({0}) : {1}>".format(self.id, self.name)
    
    def how_many_teams(self):
        return len(self.team_set.all())

class Team(models.Model):
    """
    Team model
    """
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('created at')
    updated_at = models.DateTimeField('updated at')

    def __str__(self):
        return "<Team({0}) : {1}>".format(self.id, self.name)
