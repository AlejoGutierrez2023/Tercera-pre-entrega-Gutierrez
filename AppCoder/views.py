from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
from AppCoder.forms import *
# Create your views here.

# def agrega_curso(request):
#     context = Curso(nombre = "Python", camada = "48601")
#     context.save()
#     documento_de_texto = f"---> Curso: {context.nombre}  Camada: {context.camada}"

#     return HttpResponse(documento_de_texto)

def inicio(request):
    return render(request, "AppCoder/inicio.html", {"pag": "inicio"})

def cursos(request):
    return render(request, "AppCoder/cursos.html", {"pag": "cursos"})

def profesores(request):
    return render(request, "AppCoder/profesores.html", {"pag": "profesores"})

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html", {"pag": "estudiantes"})

def entregables(request):
    return render(request, "AppCoder/entregables.html", {"pag": "entregables"})



def curso_Formulario(request):

    if request.method == "POST":

            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                context = Curso(nombre=informacion["context"], camada=informacion["camada"])
                context.save()
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

def estudiante_Formulario(request):
    if request.method == 'POST':

        miFormulario = EstudianteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            estudiante = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'],
                                email=informacion['email'])
            
            estudiante.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario= EstudianteFormulario()
        return render(request, "AppCoder/estudiante_Formulario.html", {"miFormulario":miFormulario})
    
    

def buscar(request):
    miFormulario = BuscarCursoForm()
    if request.method == "GET":
        camada = request.GET.get("camada")
        if camada:
            try:
                camada_int = int(camada)
            except ValueError:
                camada_int = None
            if camada_int is not None:
                camadas = Curso.objects.filter(camada=camada_int)
                return render(request, "AppCoder/resultados_busqueda.html", {"data": camadas})
    else:
        miFormulario = BuscarCursoForm()

    return render(request, "AppCoder/resultados_busqueda.html", {"miFormulario": miFormulario})


"""
El código define una función llamada "buscar" que recibe un objeto "request" como parámetro.

La primera línea crea un objeto "miFormulario" de la clase "BuscarCursoForm" para ser utilizado más adelante.

Luego, se verifica si el método de la solicitud HTTP es GET. 
Si es así, se extrae el valor del parámetro "camada" de la consulta GET utilizando el método "get()" del objeto "request". 
Si se encuentra un valor para "camada", se intenta convertir a un entero utilizando el bloque try-except. 
Si la conversión es exitosa, se filtran los cursos de la base de datos que tienen la misma camada que el valor proporcionado, y se pasan a la plantilla "resultados_busqueda.html" para ser renderizados. 
Los datos se pasan en un diccionario con la clave "data".

Si el método HTTP no es GET, se asigna de nuevo el objeto "miFormulario" a la instancia de la clase "BuscarCursoForm".

Por último, la función renderiza la plantilla "resultados_busqueda.html" y pasa el objeto "miFormulario" como contexto.
"""
