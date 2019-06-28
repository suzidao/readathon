from django.shortcuts import render

from .models import Book

def index(request):
  library = Book.objects.order_by('-author')
  context = {'library': library}
  return render(request, 'books/index.html', context)