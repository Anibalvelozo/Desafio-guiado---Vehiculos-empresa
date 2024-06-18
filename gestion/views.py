from django.shortcuts import get_object_or_404
from .models import Vehiculo, Chofer, RegistroContable

def crear_vehiculo(placa, modelo, ano):
    vehiculo = Vehiculo.objects.create(placa=placa, modelo=modelo, ano=ano)
    return vehiculo

def crear_chofer(nombre, licencia_conducir):
    chofer = Chofer.objects.create(nombre=nombre, licencia_conducir=licencia_conducir)
    return chofer

def crear_registro_contable(vehiculo_id, costo):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    registro = RegistroContable.objects.create(vehiculo=vehiculo, costo=costo)
    return registro

def deshabilitar_chofer(chofer_id):
    chofer = get_object_or_404(Chofer, id=chofer_id)
    chofer.habilitado = False
    chofer.save()
    return chofer

def deshabilitar_vehiculo(vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    vehiculo.habilitado = False
    vehiculo.save()
    return vehiculo

def habilitar_chofer(chofer_id):
    chofer = get_object_or_404(Chofer, id=chofer_id)
    chofer.habilitado = True
    chofer.save()
    return chofer

def habilitar_vehiculo(vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    vehiculo.habilitado = True
    vehiculo.save()
    return vehiculo

def obtener_vehiculo(vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    return vehiculo

def obtener_chofer(chofer_id):
    chofer = get_object_or_404(Chofer, id=chofer_id)
    return chofer

def asignar_chofer_a_vehiculo(vehiculo_id, chofer_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    chofer = get_object_or_404(Chofer, id=chofer_id)
    vehiculo.chofer = chofer
    vehiculo.save()
    return vehiculo

def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        print(f'Placa: {vehiculo.placa}, Modelo: {vehiculo.modelo}, Año: {vehiculo.ano}, Chofer: {vehiculo.chofer}, Habilitado: {vehiculo.habilitado}')
    return vehiculos
