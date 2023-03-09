from django.urls import path,include
from myapp import views

urlpatterns = [
    path('inicio',views.inicio),
    path("pacientes", views.pacientes, name="Paciente"),
    path("turnos", views.turnos, name="Turno"),
    path("doctores", views.doctores, name="Doctor"),
    path ('formularioPaciente', views.formularioPaciente, name="FormularioPaciente"),
    path ('formularioTurno', views.formularioTurno, name="FormularioTurno"),
    path ('formularioDoctor', views.formularioDoctor, name="FormularioDoctor"),
    path ('busquedaDoctor', views.busquedaDoctor, name="BusquedaDoctor"),
    path ('buscar/',views.buscar),
]