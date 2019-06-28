from django.shortcuts import render

from readathon.readers.models import Reader, BookList
from readathon.books.models import Book

def index(request):
  participants = Reader.objects.order_by('name')
  library = Book.objects.order_by('title')
  context = {'participants': participants, 'library': library}
  return render(request, 'index.html', context)
