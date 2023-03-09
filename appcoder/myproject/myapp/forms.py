from django import forms

class FormularioDoctor(forms.Form):
    
    apellido= forms.CharField()
    especialidad= forms.CharField()
    

class FormularioPaciente(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    obraSocial=forms.CharField()

class FormularioTurno(forms.Form):
    nomPaciente=forms.CharField()
    fecha=forms.DateField()
    especial=forms.CharField()