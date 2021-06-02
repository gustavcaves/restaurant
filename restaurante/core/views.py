from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Categoria, Plato


# def home(request):
#     return render(request, "core/home.html")

# def sample(request):
#     return render(request, "core/sample.html")

class HomePageView(TemplateView):

    template_name = "core/home.html"

class CategoriasView(ListView):

    model = Categoria

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Categorías'
        context["object_list2"] = Plato.objects.all()
        return context
    

# class PlatosView(ListView):

#     model = Plato


# def listar_platos(request):
#     platos = Plato.objects.all()
#     categorias = Categoria.objects.all()
#     return render(request, "core/listar_platos.html",context={' platos ': platos ,'categorias':categorias})