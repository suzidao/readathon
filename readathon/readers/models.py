from django.db import models
from readathon.core.models import TimeStampedModel

class Reader(TimeStampedModel):
  name = models.CharField(max_length = 200)
  target = models.IntegerField(default=0, blank=True, null=True)
