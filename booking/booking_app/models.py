from unicodedata import name
from django.db import models


class ConferenceRoom(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    projector_availbity = models.BooleanField(default=False)
