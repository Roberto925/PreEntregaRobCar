from django.db import models

class Paciente(models.Model):
    id=models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    obraSocial= models.CharField(max_length=30)

class Doctor(models.Model):
    id=models.AutoField(primary_key=True)
    
    apellido= models.CharField(max_length=30)
    especialidad= models.CharField(max_length=30)
    

class Turnos(models.Model):
    id=models.AutoField(primary_key=True)
    nomPaciente= models.CharField(max_length=30)
    fecha= models.DateField()
    especial= models.CharField(max_length=30)

# Create your models here.
