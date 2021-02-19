from django.contrib import admin

from main.models import Author, Genre, Book

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)