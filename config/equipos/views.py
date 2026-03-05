from django.shortcuts import render, get_object_or_404
from .models import Equipo, Jugador

# Create your views here.

def selector_equipos(request):
    """Vista para elegir entre los equipos registrados"""
    equipos = Equipo.objects.all()
    return render(request, 'equipos/selector.html', {'equipos': equipos})

def home_equipo(request, slug_equipo):
    """Vista de aterrizaje para un equipo específico"""
    equipo = get_object_or_404(Equipo, slug=slug_equipo)
    estrellas = Jugador.objects.filter(equipo=equipo, es_estrella=True)
    return render(request, 'equipos/home.html', {
        'equipo': equipo, 
        'estrellas': estrellas
    })

def roster_equipo(request, slug_equipo):
    """Vista para ver todos los jugadores de un equipo"""
    equipo = get_object_or_404(Equipo, slug=slug_equipo)
    jugadores = Jugador.objects.filter(equipo=equipo).order_by('numero')
    return render(request, 'equipos/roster.html', {
        'equipo': equipo, 
        'jugadores': jugadores
    })