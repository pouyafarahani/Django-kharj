from django import forms
from .models import RegisterModel


class RegisterForms(forms.ModelForm):
    class Meta:
        model = RegisterModel
        fields = ('username', 'password')


# class LogInForms(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
