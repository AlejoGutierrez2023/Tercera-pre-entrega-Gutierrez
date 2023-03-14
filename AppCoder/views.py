from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
from AppCoder.forms import *
# Create your views here.

def agrega_curso(request):
    curso = Curso(nombre = "Python", camada = "48601")
    curso.save()
    documento_de_texto = f"---> Curso: {curso.nombre}  Camada: {curso.camada}"

    return HttpResponse(documento_de_texto)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")



def curso_Formulario(request):

    if request.method == "POST":

            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                curso.save()
                return render(request, "AppCoder/inicio.html")
    else:
            miFormulario = CursoFormulario()

    return render(request, "AppCoder/curso_Formulario.html", {"miFormulario": miFormulario})


def profesor_Formulario(request):
    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'],
                                email=informacion['email'], profesion=informacion['profesion'])
            
            profesor.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario= ProfesorFormulario()
        return render(request, "AppCoder/profesor_Formulario.html", {"miFormulario":miFormulario})
