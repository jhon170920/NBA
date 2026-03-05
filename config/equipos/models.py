from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="Ejemplo: boston-celtics")
    logo = models.ImageField(upload_to='logos/')
    color_principal = models.CharField(max_length=7, default="#007A33", help_text="Hexadecimal")
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores')
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()
    posicion = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='jugadores/', null=True, blank=True)
    es_estrella = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - {self.equipo.nombre}"