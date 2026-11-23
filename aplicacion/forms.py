from django import forms
from aplicacion.models import Videojuego, Solicitud


class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = [
            'titulo',
            'descripcion',
            'genero',
            'modalidad_trato',
            'tiempo_uso',
            'valor_estimado',
            'imagen',
            'plataforma',
        ]

    titulo = forms.CharField()
    descripcion = forms.CharField()
    genero = forms.CharField()
    modalidad_trato = forms.CharField()
    tiempo_uso = forms.CharField()
    valor_estimado = forms.IntegerField()
    imagen = forms.ImageField(required=False)

    titulo.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['class'] = 'form-control'
    genero.widget.attrs['class'] = 'form-control'
    genero.widget.attrs['placeholder'] = 'ej: rpg, accion, terror'
    modalidad_trato.widget.attrs['class'] = 'form-control'
    modalidad_trato.widget.attrs['placeholder'] = 'compra o permuta'
    tiempo_uso.widget.attrs['class'] = 'form-control'
    tiempo_uso.widget.attrs['placeholder'] = 'ej: 2 semanas, 3 meses'
    valor_estimado.widget.attrs['class'] = 'form-control'
    imagen.widget.attrs['class'] = 'form-control'


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['tipo_interes', 'mensaje']

    tipo_interes = forms.CharField()
    mensaje = forms.CharField(required=False)

    tipo_interes.widget.attrs['class'] = 'form-control'
    tipo_interes.widget.attrs['placeholder'] = 'compra o permuta'
    mensaje.widget.attrs['class'] = 'form-control'
    mensaje.widget.attrs['placeholder'] = 'opcional'