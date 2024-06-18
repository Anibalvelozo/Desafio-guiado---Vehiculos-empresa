from django.db import models

class Chofer(models.Model):
    nombre = models.CharField(max_length=100)
    licencia_conducir = models.CharField(max_length=15)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    placa = models.CharField(max_length=10)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    habilitado = models.BooleanField(default=True)
    chofer = models.ForeignKey(Chofer, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.placa

class RegistroContable(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Registro de {self.vehiculo.placa} en {self.fecha}'
