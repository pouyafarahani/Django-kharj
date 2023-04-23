from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import RegisterForms

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages


class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        form = RegisterForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user = User.objects.create_user(cd['username'], None, cd['password'])
                messages.success(request, f'khoshomdi {cd["username"]}')
                login(request, user)
            except:
                messages.warning(request, 'in username ghabln sabtname karde :)')
                return render(request, 'accounts/register.html', {'form': form})
            return render(request, 'home/home.html')
        else:
            return render(request, 'accounts/register.html', {'form': form})


class LogInView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        form = RegisterForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                messages.success(request, f'khoshomdi {cd["username"]}')
                login(request, user)
                return redirect('home:home')
            return redirect('accounts:login')
