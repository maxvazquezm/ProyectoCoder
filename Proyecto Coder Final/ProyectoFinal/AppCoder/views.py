from django.shortcuts import render
from .models import Curso

from .forms import CursoFormulario
from .models import Curso
# Create your views here.


from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView



def inicio_view(request):
    return render(request, "AppCoder/inicio.html")


def cursos_view(request):
    if request.method == "GET":
        print("+" * 90) #  Imprimimos esto para ver por consola
        print("+" * 90) #  Imprimimos esto para ver por consola
        return render(
            request,
            "AppCoder/curso_formulario_avanzado.html",
            {"form": CursoFormulario()}
        )
    else:
        print("*" * 90)     #  Imprimimos esto para ver por consola
        print(request.POST) #  Imprimimos esto para ver por consola
        print("*" * 90)     #  Imprimimos esto para ver por consola

        modelo = Curso(curso=request.POST["curso"], camada=request.POST["camada"])
        modelo.save()
        return render(
            request,
            "AppCoder/inicio.html",
        )


