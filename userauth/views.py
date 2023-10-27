import pyotp
from django.shortcuts import render
from django.views.generic import TemplateView


class userauth_login(TemplateView):
    template_name = 'login.html'


def login(request):
    if request.method == "POST":
        otp = request.POST['otp']
        secret_key = 'XUAWQPA34OWLJVYRF7KAOHSEBTRJ4PBA'
        token = pyotp.TOTP(secret_key)
        auth_otp = token.now()
        if otp == auth_otp:
            return render(request, 'dashboard.html')
        return render(request, 'authentication-forgot-password.html')


