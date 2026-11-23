from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from aplicacion.models import Videojuego, Solicitud
from aplicacion.forms import VideojuegoForm, SolicitudForm


@login_required
def inicio(request):
    videojuegos = Videojuego.objects.all()
    solicitudes = Solicitud.objects.filter(cliente=request.user)
    datos = {
        'videojuegos': videojuegos,
        'solicitudes': solicitudes,
    }
    return render(request, 'inicio.html', datos)


@login_required
def publicar_videojuego(request):
    form = VideojuegoForm()
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, request.FILES)
        if form.is_valid():
            videojuego = form.save(commit=False)
            videojuego.dueno = request.user
            videojuego.save()
            return redirect('inicio')
    datos = {'form': form}
    return render(request, 'publicar_videojuego.html', datos)


@login_required
def crear_solicitud(request, videojuego_id):
    videojuego = Videojuego.objects.get(id=videojuego_id)
    form = SolicitudForm()
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.videojuego = videojuego
            solicitud.cliente = request.user
            solicitud.estado = 'Pendiente'
            solicitud.save()
            return redirect('inicio')
    datos = {'form': form, 'videojuego': videojuego}
    return render(request, 'crear_solicitud.html', datos)


def registro(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('inicio')
    datos = {'form': form}
    return render(request, 'registration/registro.html', datos)