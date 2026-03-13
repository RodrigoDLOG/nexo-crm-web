from django.forms import ModelForm
from django import forms
from .models import Poliza

class PolizaForm(ModelForm):
    class Meta:
        model = Poliza
        fields = [
            'aseguradoraid',
            'agenteid',
            'clienteid',
            'tipopolizaid',
            'formapagoid',
            'metodopagoid',
            'prima',
            'fechafin',
        ]
        widgets = {
            'fechafin': forms.DateInput(attrs={'type': 'date'}),
        }