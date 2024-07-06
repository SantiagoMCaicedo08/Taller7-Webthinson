from django import forms
from .models import Tipodocumento, Persona

class TipodocumentoForm(forms.ModelForm):
    class Meta:
        model = Tipodocumento
        fields = ['nombre', 'descripcion']

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'documento', 'lugarresidencia', 'fechanacimiento', 'email', 'telefono', 'usuario', 'password']
