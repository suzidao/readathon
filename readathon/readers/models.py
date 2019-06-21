from django.db import models
from readathon.core.models import TimeStampedModel
from readathon.books.models import Book

class Reader(TimeStampedModel):
  name = models.CharField()
  books = models.ManyToManyField(Book)
  target = models.CharField(null=True, blank=True, default=None)