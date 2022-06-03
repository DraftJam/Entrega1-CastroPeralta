from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    path("equipos", views.equipos, name = "equipos"),
    path("jugadores", views.jugadores, name = "jugadores"),
    path("entrenadores", views.entrenadores, name = "entrenadores"),
    path("buscar", views.buscar, name="buscar"),
    path("alta_jugador", views.registrado),
    path("busqueda", views.busqueda)
]