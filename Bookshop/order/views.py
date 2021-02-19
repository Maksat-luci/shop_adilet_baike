from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from order.forms import CreateOrderForm
from order.models import Order




def create_order(request):
    request.POST
    order_form = CreateOrderForm(request.POST)
    if order_form.is_valid():
        order = Order.objects.create(**order_form.cleaned_data)
        return HttpResponse('succesfully created order')
    return render(request, 'order.html', {'form':order_form})

