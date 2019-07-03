from django import forms

from .models import Reader

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Reader
        fields = ('name', 'target',)
