from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=1000, verbose_name="Descripción", default="Add Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorias"

class Plato(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Plato"
        verbose_name_plural = "Platos"