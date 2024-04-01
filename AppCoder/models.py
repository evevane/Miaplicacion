from django.db import models

# Create your models here.


class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} camada: {self.camada}"


    
    

class Profesores(models.Model):
    
    nombre = models.CharField(max_length=40)
    materia = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Nombre: {self.nombre} materia: {self.materia}"






class Alumnos(models.Model):
    
    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} dni: {self.dni}"
