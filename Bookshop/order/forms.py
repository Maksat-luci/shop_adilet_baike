from django import forms

from main.models import Book


class CreateOrderForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all())
    phone= forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    city = forms.CharField(max_length=50)

