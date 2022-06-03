from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import *
from app_coder.forms import *

# Create your views here.

def inicio(request):
    return render(request, "plantillas.html")

def equipos(request):
    if request.method == "POST":

        mi_formulario = Equipo_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
  
        equipo = Equipo(nombre = datos['nombre'], fundacion = datos['fundacion'])
        equipo.save()
        return render(request, "equipos.html")

    return render(request, "equipos.html")


def jugadores(request):
    if request.method == "POST":

        mi_formulario = Jugador_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
  
        jugador = Jugador(nombre = datos['nombre'], nacimiento = datos['nacimiento'])
        jugador.save()
        return render(request, "jugadores.html")

    return render(request, "jugadores.html")


def entrenadores(request):
    if request.method == "POST":

        mi_formulario = Entrenador_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
  
        entrenador = Entrenador(nombre = datos['nombre'], nacimiento = datos['nacimiento'])
        entrenador.save()
        return render(request, "entrenadores.html")

    return render(request, "entrenadores.html")

def buscar(request):
    return render(request,"buscar.html")

def registrado(request):
    return render(request, "registrado.html")

def busqueda(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        jugadores = Jugador.objects.filter(nombre__icontains = nombre)

        return render(request, "resultado_busqueda.html", {"jugadores": jugadores})

    else:
        return HttpResponse("Campo Vacio")
    return HttpResponse(f"Estamos buscando la siguiente información: {request.GET['nombre']}")
