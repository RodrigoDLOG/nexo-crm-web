from django.forms import ModelForm
from django import forms
from .models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre', 'appaterno', 'apmaterno', 'fechanacimiento', 'rfc', 'curp',
            'generoid', 'celular', 'telefono', 'correo', 'codigopostal', 'pais',
            'estado', 'municipio', 'ciudad', 'colonia', 'calle', 'numcasa'
        ]
        widgets = {
            'fechanacimiento': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'correo': forms.EmailInput(attrs={'placeholder': 'cliente@gmail.com', 'maxlength': '100'}),
            'celular': forms.TextInput(attrs={'placeholder': '8112345678', 'maxlength': '10'}),
            'telefono': forms.TextInput(attrs={'placeholder': '8187654321', 'maxlength': '10'}),
            'rfc': forms.TextInput(attrs={'maxlength': '13'}),
            'curp': forms.TextInput(attrs={'maxlength': '18'}),
            'codigopostal': forms.TextInput(attrs={'maxlength': '5'}),
            'nombre': forms.TextInput(attrs={'maxlength': '50'}),
            'appaterno': forms.TextInput(attrs={'maxlength': '50'}),
            'apmaterno': forms.TextInput(attrs={'maxlength': '50'}),
            'pais': forms.TextInput(attrs={'maxlength': '50'}),
            'estado': forms.TextInput(attrs={'maxlength': '50'}),
            'municipio': forms.TextInput(attrs={'maxlength': '50'}),
            'ciudad': forms.TextInput(attrs={'maxlength': '50'}),
            'colonia': forms.TextInput(attrs={'maxlength': '50'}),
            'calle': forms.TextInput(attrs={'maxlength': '50'}),
            'numcasa': forms.TextInput(attrs={'maxlength': '50'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.fechanacimiento:
            self.fields['fechanacimiento'].initial = self.instance.fechanacimiento.strftime('%Y-%m-%d')
        
        self.fields['apmaterno'].required = False
        self.fields['rfc'].required = False
        self.fields['curp'].required = False

        # --- INICIO DE LA CORRECCIÓN ---
        # Este bucle recorre todos los campos del formulario
        # y les añade la clase 'form-control' de Bootstrap.
        # Esto es crucial para que los estilos se apliquen correctamente.
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        # --- FIN DE LA CORRECCIÓN ---

    def clean_apmaterno(self):
        data = self.cleaned_data.get('apmaterno')
        return data if data else 'X'

    def clean_rfc(self):
        data = self.cleaned_data.get('rfc')
        return data if data else 'X'

    def clean_curp(self):
        data = self.cleaned_data.get('curp')
        return data if data else 'X'