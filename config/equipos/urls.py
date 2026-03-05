from django.urls import path
from . import views

urlpatterns = [
    # Ruta para el selector de equipos (página principal)
    path('', views.selector_equipos, name='selector'),
    
    # Ruta dinámica para la home de cada equipo
    path('<slug:slug_equipo>/', views.home_equipo, name='home_equipo'),
    
    # Ruta para el roster del equipo
    path('<slug:slug_equipo>/roster/', views.roster_equipo, name='roster'),
]