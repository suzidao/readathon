from django.shortcuts import render, redirect

from .models import Book
from .forms import BookForm

def index(request):
  library = Book.objects.order_by('-author')
  context = {'library': library}
  return render(request, 'books/index.html', context)

def add_book(request):
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      book = form.save(commit=False)
      book.save()
      return redirect('/books')
  else:
    form = BookForm()
  
  context = {'form': form}
  return render(request, 'books/add.html', context)  