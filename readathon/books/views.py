from django.shortcuts import render

from .models import Book
from .forms import BookForm

def index(request):
  library = Book.objects.order_by('-author')
  context = {'library': library}
  return render(request, 'books/index.html', context)

def add_book(request):
  form = BookForm()
  context = {'form': form}
  return render(request, 'books/add.html', context)  