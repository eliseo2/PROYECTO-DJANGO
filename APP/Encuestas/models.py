from django.db import models

class Pregunta(models.Model):
    texto_pregunta = models.Charfield(max_lenght=200)
    fecha_pub = models.DateTimeField("Fecha de publicación")

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_opcion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

# Create your models here.
