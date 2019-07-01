from django.contrib import admin

from .models import Book, BookList

admin.site.register(Book)
admin.site.register(BookList)