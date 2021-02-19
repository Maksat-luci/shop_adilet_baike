from django.shortcuts import render

# Create your views here.
from main.models import Book, Genre
from django.db.models import Q


def index(request):
    genres = Genre.objects.all()

    return render(request,'index.html',{'genres':genres})

def books_list(request,slug):
    books_list = Book.objects.filter(genre__slug=slug)
    return render(request,'books_list.html',{'books':books_list})