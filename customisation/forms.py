from django import forms
from .models import AccessoryRequest


# map the html form to the fields on the AccessoryRequest model
# for the backend form validation
class AccessoryRequestForm(forms.ModelForm):
    class Meta:
        model = AccessoryRequest
        fields = ['name', 'colour', 'type', 'description', 'image']
