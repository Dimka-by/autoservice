from django import forms
from .models import *


class AddClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'car']