from django.db import models
from django.contrib.auth.admin import User

# Create your models here.
class Business(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, verbose_name = 'Usuario', unique = True)
    business = models.CharField(max_length = 100, verbose_name = 'Nombre de la Empresa', unique = True)
    description = models.TextField(verbose_name= 'description', null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "empresa"
        verbose_name_plural = "empresas"
        ordering = ['-created']

    def __str__(self):
        return self.business