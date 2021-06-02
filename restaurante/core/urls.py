from django.urls import path
from . import views
from core.views import HomePageView
from core.views import CategoriasView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomePageView.as_view(), name='home'),
    # path('sample/', views.sample, name="sample"),
    path('categorias/', CategoriasView.as_view(), name="detalle_categoria" ),
    # path('platos/', PlatosView.as_view(), name="detalle_platos" ),
    # path('listarplatos/', views.listar_platos, name="listar_platos")
]