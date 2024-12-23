from django import forms
from .models import RockAdoption


# Form created in the backend on the basis of the RockAdoption model,
# displayed on the adoption-form template
class AdoptionForm(forms.ModelForm):
    class Meta:
        model = RockAdoption
        fields = ('full_name', 'address1', 'address2',
                  'town', 'postcode', 'country')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field -
        - code from the Code Institute's Boutique Ado
        student project
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full name',
            'address1': 'Street address',
            'address2': 'Street address line 2',
            'postcode': 'Postcode / ZIP code',
            'town': 'City',
            'country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
