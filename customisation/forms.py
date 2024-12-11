from django import forms
from .models import AccessoryRequest


class AccessoryRequestForm(forms.ModelForm):
    class Meta:
        model = AccessoryRequest
        fields = ['name', 'colour', 'type', 'description', 'image']
