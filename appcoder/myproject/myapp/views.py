from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Doctor,Paciente,Turnos
from .forms import FormularioDoctor,FormularioPaciente,FormularioTurno
def inicio(request):
    return render(request, 'inicio.html')

def pacientes(request):
    return render(request, 'pacientes.html')
def turnos(request):
    return render(request, 'turnos.html')
def doctores(request):
    return render(request, 'doctores.html')

def formularioPaciente(request):
    if request.method=='POST':
        miFormulario=FormularioPaciente(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            paciente= Paciente(nombre=informacion['nombre'],apellido=informacion['apellido'],obraSocial=informacion['obraSocial'])
            paciente.save()
            return render(request,'inicio.html')
        else:
            miFormulario=FormularioTurno()

    return render(request, "formularioPaciente.html")

def formularioDoctor(request):
    if request.method=='POST':
        miFormulario=FormularioDoctor(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            doctor= Doctor(nombre=informacion['nombre'],apellido=informacion['apellido'],especialidad=informacion['especialidad'])
            doctor.save()
            return render(request,'inicio.html')
        else:
            miFormulario=FormularioTurno()
        
    return render(request, "formularioDoctor.html")

def formularioTurno(request):
    if request.method=='POST':
        miFormulario=FormularioTurno(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            turno= Turnos(nomPaciente=informacion['nomPaciente'],fecha=informacion['fecha'],especial=informacion['especial'])
            turno.save()
            return render(request,'inicio.html')
        else:
            miFormulario=FormularioTurno()
        
    return render(request, "formularioTurno.html",)

def busquedaDoctor(request):
    return render(request, 'busquedaDoctor.html')

def buscar(request):
    if request.GET['especialidad']:
        especialidad= request.GET['especialidad']
        doctor=Doctor.objects.filter(especilidad__iconteins= especialidad)

        return render(request, 'resultadoBusqueda.html', {"doctor": doctor, "especialidad": especialidad})
    else:
        respuesta="No enviaste Datos."
    
    return HttpResponse(respuesta)
# Create your views here.