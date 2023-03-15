from django.urls import path
from AppCoder import views
urlpatterns = [

    path("", views.inicio, name="Inicio"),
    path("cursos", views.cursos, name = "Cursos"),
    path("profesores", views.profesores, name="Profesores"),
    path("estudiantes", views.estudiantes, name="Estudiantes"),
    path("entregables", views.entregables, name="Entregables"),
    path('curso_Formulario', views.curso_Formulario, name="CursoFormulario"),
    path('profesor_Formulario', views.profesor_Formulario, name="ProfesorFormulario"),
    path('estudiante_Formulario', views.estudiante_Formulario, name="EstudianteFormulario"),
    path("busqueda_curso", views.buscar_curso, name= 'BusquedaCurso'),


]