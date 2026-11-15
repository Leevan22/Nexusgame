from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Videojuego, Solicitud
from .forms import VideojuegoForm, SolicitudForm

@login_required
def inicio(request):
    videojuegos = Videojuego.objects.all()
    solicitudes_usuario = Solicitud.objects.filter(cliente=request.user)
    return render(request, 'inicio.html', {
        'videojuegos': videojuegos,
        'solicitudes_usuario': solicitudes_usuario
    })

@login_required
def publicar_videojuego(request):
    if request.method == 'POST':
        # ¡Aquí está la clave! Agregamos request.FILES para capturar la imagen
        form = VideojuegoForm(request.POST, request.FILES)
        if form.is_valid():
            videojuego = form.save(commit=False)
            videojuego.dueno = request.user
            videojuego.save()
            return redirect('inicio')
    else:
        form = VideojuegoForm()
    return render(request, 'publicar_videojuego.html', {'form': form})

@login_required
def crear_solicitud(request, videojuego_id):
    videojuego = get_object_or_404(Videojuego, id=videojuego_id)
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.cliente = request.user
            solicitud.videojuego = videojuego
            solicitud.save()
            return redirect('inicio')
    else:
        form = SolicitudForm()
    return render(request, 'crear_solicitud.html', {'form': form, 'videojuego': videojuego})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})