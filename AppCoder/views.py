from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import curso_formulario
from AppCoder.models import Profesores
from AppCoder.forms import profesores_formulario
from AppCoder.models import Alumnos
from AppCoder.forms import alumnos_formulario

# Create your views here.

def inicio(request):
    return render( request , "padre.html")




def alta_curso(request,nombre):
    curso = Curso(nombre=nombre , camada=12342)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)


def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def alumnos(request):
    return render(request , "alum_img.html")


def curso_formulario(request):

    if request.method == "post":
    
        mi_formulario = curso_formulario( request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            
        return render(request , "formulario.html" )
    return render(request , "formulario.html")  





def buscar_curso(request):
    
    return render(request, "buscar_curso.html")  

 



def buscar(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]

        cursos = Curso.objects.filter(nombre__icontains= nombre)

        return render( request , "resultado_busqueda.html" , {"cursos":cursos})

    else:

        return HttpResponse("Ingrese el nombre del curso")
    





def elimina_curso(request , id ):
    curso = curso.objects.get(id=id) 
    curso.delete()  
    
    curso = Curso.objects.all()


    return render(request , "cursos.html" , {"cursos":curso})



def editar(request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = curso_formulario( request.POST )

        if mi_formulario.is_valid():

            datos = mi_formulario.cleaned_data

            curso.nombre = datos["nombre"]

            curso.camada = datos["camada"]

            curso.save()

            curso = Curso.objects.all()

            return render(request , "cursos.html" , {"cursos":curso})

 

        

    else:

        mi_formulario = curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})

    

    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})





def inicio(request):
    return render( request , "padre.html")




def alta_profesores(request,nombre):
    profesores = Profesores(profesores=nombre , materia="")
    profesores.save()
    texto = f"Se guardo en la BD de profesores : {profesores.nombre} {profesores.materia}"
    return HttpResponse(texto)


def ver_profesores(request):
    profesores = Profesores.objects.all()
    dicc = {"profesores": profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)




def profesores_formulario(request):

    if request.method == "post":
    
        mi_formulario = profesores_formulario( request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesores = Profesores( nombre=datos["nombre"] , materia=datos["materia"])
            profesores.save()
            
        return render(request , "formulario_prof.html" )
    return render(request , "formulario_prof.html")  








def inicio(request):
    return render( request , "padre.html")




def alta_alumnos(request,nombre):
    alumnos = alumnos(nombre=nombre , dni=12342)
    alumnos.save()
    texto = f"Se guardo en la BD de alumnos: {alumnos.nombre} {alumnos.dni}"
    return HttpResponse(texto)


def ver_alumnos(request):
    alumnos = Alumnos.objects.all()
    dicc = {"alumnos": alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)



def alumnos_formulario(request):

    if request.method == "post":
    
        mi_formulario = alumnos_formulario( request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumnos = alumnos( nombre=datos["nombre"] , dni=datos["dni"])
            alumnos.save()
            
        return render(request , "formulario_alumnos.html" )
    return render(request , "formulario_alumnos.html")  



def buscar_alumno(request):
    
    return render(request, "buscar_alumno.html")  

 

def buscar_alumno(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]

        alumnos = alumnos.objects.filter(nombre__icontains= nombre)

        return render( request , "resultado_busq_alum.html" , {"alumnos":alumnos})

    else:

        return HttpResponse("Ingrese el nombre del alumno")