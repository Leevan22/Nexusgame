from django.db import models
from django.contrib.auth.models import User

class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Videojuego(models.Model):
    MODALIDAD_CHOICES = [
        ('Venta', 'Venta'),
        ('Permuta', 'Permuta'),
        ('Ambos', 'Venta o Permuta'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    genero = models.CharField(max_length=100)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    valor_estimado = models.PositiveIntegerField(verbose_name="Valor estimado ($)")
    tiempo_uso = models.CharField(max_length=100, help_text="Ej: 3 meses, 2 semanas")
    modalidad_trato = models.CharField(max_length=50, choices=MODALIDAD_CHOICES)
    imagen = models.ImageField(upload_to='videojuegos/', verbose_name="Imagen del juego")
    dueno = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Estandariza automáticamente el texto (ej: "3 semanas" o "3 SEMANAS" pasa a "3 Semanas")
        if self.tiempo_uso:
            self.tiempo_uso = self.tiempo_uso.strip().title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

class Solicitud(models.Model):
    TIPO_CHOICES = [
        ('Compra', 'Compra'),
        ('Permuta', 'Permuta'),
    ]

    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitudes_enviadas')
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE, related_name='solicitudes')
    tipo_interes = models.CharField(max_length=50, choices=TIPO_CHOICES)
    mensaje = models.TextField()
    estado = models.CharField(max_length=50, default='Pendiente')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente.username} - {self.videojuego.titulo}"