from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="Ejemplo: boston-celtics") #se usa para crear URL con el texto ingresado
    logo = models.ImageField(upload_to='logos/') #para usar imagenes se instalo Pillow
    color_principal = models.CharField(max_length=7, default="#007A33", help_text="Hexadecimal") #Color del equipo se usara para el color de la pagina
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores') #permite que al crear jugador este se asocie a un equipo // Ademas de que si se elimina un equipo tambien se elimina sus jugadores 
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField() #IntegerField se usa para numeros enteros, no decimales, para decimales usar DecimalFiled
    posicion = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='jugadores/', null=True, blank=True) #para usar imagenes se instalo Pillow
    es_estrella = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - {self.equipo.nombre}"