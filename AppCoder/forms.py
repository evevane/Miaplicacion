from django import forms


class curso_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    

class profesores_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    materia = forms.CharField(max_length=30)
    

class alumnos_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    dni = forms.IntegerField()