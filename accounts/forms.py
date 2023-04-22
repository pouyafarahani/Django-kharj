from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class RegisterForms(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class LogInForms(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
