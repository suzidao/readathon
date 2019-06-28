from django.db import models
from readathon.core.models import TimeStampedModel

class Reader(TimeStampedModel):
  name = models.TextField()
  target = models.TextField(null=True, blank=True, default=None)

class BookList(models.Model):
  reader = models.ForeignKey(Reader, on_delete=models.CASCADE)