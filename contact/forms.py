# https://docs.djangoproject.com/en/5.1/ref/forms/widgets/

from django.core.exceptions import ValidationError
from django import forms

from . import models

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Your name...'
        })
        
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Your last name...'
        })
    
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )
        # widgets = {
        #     'first_name': forms.PasswordInput()
        # } #muda os widgets dos input
        
    
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if last_name == first_name:
            
            msg = ValidationError(
                'Last name cannot be the same as first name',
                code='invalid'
            )
            
            self.add_error('last_name', msg)
        
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Mensagem de erro',
                    code='invalid'
                )
            )
        return first_name