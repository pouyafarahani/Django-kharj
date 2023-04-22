from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import RegisterModel


class RegisterForms(forms.ModelForm):
    class Meta:
        model = RegisterModel
        fields = ('username', 'password')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(email=username).exists():
            raise ValidationError('in username ghablan sabt nam shode :)')
        return username


class LogInForms(forms.ModelForm):
    class Meta:
        model = RegisterModel
        fields = ('username', 'password')
