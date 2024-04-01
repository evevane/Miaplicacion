from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio , name="home"),
    path("ver_curso", views.ver_cursos , name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alumnos", views.alumnos , name="alumnos"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    #path("alta_profesores/<nombre>", views.alta_profesores),
    path("ver_profesores", views.ver_profesores , name="profesores"),
    path("alta_profesores", views.profesores_formulario),
    #path("alta_alumnos/<nombre>", views.alta_alumnos),
    path("ver_alumnos", views.ver_alumnos , name="alumnos"),
    path("alta_alumnos", views.alumnos_formulario),
    path("buscar_alumno", views.buscar_alumno)
]    