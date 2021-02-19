from django.contrib import admin
from django.urls import path, include

from main.views import index
from order.views import create_order

urlpatterns = [
    path('', create_order, name='create_order'),

]
