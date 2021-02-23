from django import forms
from django.contrib.auth import get_user_model

from account.utils import send_activation_mail

User = get_user_model()





class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=8,required=True,widget=forms.PasswordInput)
    password_confirmation = forms.CharField(max_length=8, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','password','password_confirmation','name','last_name')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('пользователь с таким эмейлом уже существует')
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError('пароли не совпадают!!')
        return data

    def save(self,commit=True):
        user = User.objects.create(**self.cleaned_data)#распоковываем словарь и передаём в create и добавляем в user
        send_activation_mail(user)
        return user



