from django.db import models
from readathon.core.models import TimeStampedModel
from readathon.readers.models import Reader

class Book(TimeStampedModel):
  title = models.CharField()
  author = models.CharField()
  readers = models.ManyToManyField(Reader, default=None, blank=True, null=True)
  recommender = models.ForeignKey(Reader)