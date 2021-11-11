from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput

from .models import CuentaBancaria,Persona

class BancoForm(forms.ModelForm):
    class Meta:
        model = CuentaBancaria
        fields = ('persona','numero_cuenta', 'cbu', 'alias', 'banco_emisor',)


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('dni','nombre_completo', 'fecha_nacimiento', 'sexo', 'domicilio',)