from django.contrib.auth.models import User
from .forms import RegisterForms

from django.shortcuts import render, redirect
from django.views import View


class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        form = RegisterForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], None, cd['password'])
            print('4')
            return render(request, 'home/home.html')
        print('3')
        return render(request, 'accounts/register.html', {'form': form})


class LogInView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

