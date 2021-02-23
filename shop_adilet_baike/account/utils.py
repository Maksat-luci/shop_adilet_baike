from django.core.mail import send_mail


def send_activation_mail(user):
    user.create_actiavation_code()
    message = f"""Спасибо за регистрацию.Aктивируйте свой аккаунт по ссылке 
    http://127.0.0.1:8000/accounts/activation/?u={user.activation_code}"""
    send_mail(
        'Aктивация аккаунта',
        message,
        'test@myproject.com',
        [user.email]

    )


#TODO:смена пароля
#TODO:забыли пароль
#TODO:smtp

