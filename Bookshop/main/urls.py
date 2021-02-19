from django.contrib import admin
from django.urls import path, include

from main.views import index, books_list


urlpatterns = [
    path('',index,name='home'),
    path('listing/<str:slug>/',books_list,name='books-listing')
]
