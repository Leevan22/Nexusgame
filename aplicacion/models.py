from django.db import models
from django.contrib.auth.models import User


class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    genero = models.CharField(max_length=50)
    modalidad_trato = models.CharField(max_length=50)
    tiempo_uso = models.CharField(max_length=50)
    valor_estimado = models.IntegerField()
    imagen = models.ImageField(upload_to='videojuegos/', null=True)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    dueno = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Solicitud(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_interes = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=200)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_interes + " - " + self.estado