from pyexpat import model
from django.db import models

# Create your models here.
class Equipo(models.Model):

    nombre = models.CharField(max_length=40)
    fundacion = models.IntegerField()

class Jugador(models.Model):

    nombre = models.CharField(max_length=40)
    nacimiento = models.IntegerField()

class Entrenador(models.Model):
    nombre = models.CharField(max_length=40)
    nacimiento = models.IntegerField()