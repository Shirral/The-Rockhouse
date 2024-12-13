from django import forms
from .models import Rock


class RockEditForm(forms.ModelForm):
    class Meta:
        model = Rock
        fields = [
            'name',
            'material',
            'texture',
            'personality',
            'description',
            'price'
        ]
