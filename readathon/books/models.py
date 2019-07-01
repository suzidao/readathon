from django.db import models
from readathon.core.models import TimeStampedModel
from readathon.readers.models import Reader

class BookList(models.Model):
  reader = models.ForeignKey(Reader, on_delete=models.CASCADE, null=True, blank=True, default=None)

  def __str__(self):
    return self.reader.name

class Book(TimeStampedModel):
  title = models.CharField(max_length = 5000)
  author = models.CharField(max_length = 200)
  reader = models.ForeignKey(Reader, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name = 'reader')
  recommender = models.ForeignKey(Reader, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name = 'recommender')
  book_list = models.ForeignKey(BookList, on_delete=models.CASCADE, null=True, blank=True, default=None)

  def __str__(self):
    return self.title