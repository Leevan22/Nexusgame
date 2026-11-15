from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('publicar/', views.publicar_videojuego, name='publicar_videojuego'),
    path('solicitar/<int:videojuego_id>/', views.crear_solicitud, name='crear_solicitud'),
    path('registro/', views.registro, name='registro'),
]