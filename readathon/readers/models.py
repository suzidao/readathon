from django.db import models
from readathon.core.models import TimeStampedModel

class Reader(TimeStampedModel):
  name = models.CharField()
  target = models.CharField(null=True, blank=True, default=None)