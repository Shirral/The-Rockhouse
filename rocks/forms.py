from django import forms
from .models import Rock


# form to match the front-end form on rock-edit.html
# for the back-end validation of the form
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
