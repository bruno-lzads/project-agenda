from django.core.exceptions import ValidationError
from django import forms

from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
    
    def clean(self):
        cleaned_data = self.cleaned_data
        
        self.add_error(
            'first_name',
            ValidationError(
                'Mesagem de erro',
                code='invalid'
            )
        )
        
        self.add_error(
            'last_name',
            ValidationError(
                'Mesagem de erro',
                code='invalid'
            )
        )
        
        return super().clean()