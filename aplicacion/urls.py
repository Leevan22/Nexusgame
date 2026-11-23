from django.urls import path
from aplicacion import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio),
    path('publicar/', views.publicar_videojuego, name='publicar_videojuego'),
    path('solicitar/<int:videojuego_id>/', views.crear_solicitud, name='crear_solicitud'),
    path('registro/', views.registro, name='registro'),
]