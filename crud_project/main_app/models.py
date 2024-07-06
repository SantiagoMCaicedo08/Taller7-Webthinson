from django.db import models

class Tipodocumento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipodocumento = models.ForeignKey(Tipodocumento, on_delete=models.CASCADE, null=True, blank=True)
    documento = models.CharField(max_length=20)
    lugarresidencia = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fechanacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
