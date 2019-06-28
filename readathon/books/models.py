from django.db import models
from readathon.core.models import TimeStampedModel
from readathon.readers.models import Reader, BookList

class Book(TimeStampedModel):
  title = models.TextField()
  author = models.TextField()
  recommender = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name='recommender')
  
  book_list = models.ForeignKey(BookList, on_delete=models.CASCADE)
