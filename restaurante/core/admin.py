from django.contrib import admin
from .models import Categoria, Plato

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Categoria, CategoryAdmin)

class PlatoAdmin(admin.ModelAdmin):
    list_display = ('name','categoria',)

admin.site.register(Plato,PlatoAdmin)