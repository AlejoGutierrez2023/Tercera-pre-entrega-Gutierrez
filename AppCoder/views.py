from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
# Create your views here.

def agrega_curso(request):
    curso = Curso(nombre = "Python", camada = "48601")
    curso.save()
    documento_de_texto = f"---> Curso: {curso.nombre}  Camada: {curso.camada}"

    return HttpResponse(documento_de_texto)