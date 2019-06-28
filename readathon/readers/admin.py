from django.contrib import admin

from .models import Reader, BookList

admin.site.register(Reader)
admin.site.register(BookList)