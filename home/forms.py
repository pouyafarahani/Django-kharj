from django import forms
from .models import costsModel


class costsForms(forms.ModelForm):
    class Meta:
        model = costsModel
        fields = ('name', 'explanation', 'price', 'time')

