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
    
    
def buscar_curso(request):
    if request.method == 'POST':
        form = BuscarCursoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            camada = form.cleaned_data['camada']
            resultados = Curso.objects.filter(nombre__icontains=nombre, camada=camada)
            context = {'resultados': resultados}
            try:
                context = Curso.objects.get(nombre__iexact= nombre, camada__iexact= camada )
            except Curso.DoesNotExist:
                context = None

                if context is not None:
    # Se encontraron los datos, pasar a la plantilla
                    context = {'context': context, 'encontrado': True}
                    return render(request, 'busqueda.html', context)
                else:
    # No se encontraron los datos, pasar a la plantilla
                    context = {'encontrado': False}
                    return render(request, 'busqueda.html', context)



            return render(request, "AppCoder/resultados_busqueda.html", context)
    else:
        form = BuscarCursoForm()
        resultados = None
    return render(request, 'AppCoder/buscar.html', {'form': form, 'resultados': resultados})














# def entregable_Formulario(request):
#     if request.method == 'POST':

#         miFormulario = EntregableFormulario(request.POST)
#         print(miFormulario)

#         if miFormulario.is_valid:
            
#             informacion = miFormulario.cleaned_data

#             entregable = Entregable(nombre=informacion['nombre'], fecha_de_entrega=informacion['fecha de entrega'],
#                                 entregado=informacion['entregado'])
            
#             entregable.save()

#             return render(request, "AppCoder/inicio.html")
#     else:
#         miFormulario= EntregableFormulario()
#         return render(request, "AppCoder/entregable_Formulario.html", {"miFormulario":miFormulario})