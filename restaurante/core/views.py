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

class PlatosView(ListView):

    model = Plato