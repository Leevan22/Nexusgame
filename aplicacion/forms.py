from django import forms
from .models import Videojuego, Solicitud

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['titulo', 'descripcion', 'genero', 'plataforma', 'valor_estimado', 'tiempo_uso', 'modalidad_trato', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'genero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: RPG, Acción'}),
            'plataforma': forms.Select(attrs={'class': 'form-select'}),
            'valor_estimado': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'tiempo_uso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 3 meses, 2 semanas'}),
            'modalidad_trato': forms.Select(attrs={'class': 'form-select'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['tipo_interes', 'mensaje']
        widgets = {
            'tipo_interes': forms.Select(attrs={'class': 'form-select'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Indica tu oferta o qué juego ofreces'}),
        }