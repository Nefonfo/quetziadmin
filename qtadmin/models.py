from django.db import models
from django.contrib.auth.admin import User
# Create your models here.

class QuetziAdmin(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, verbose_name = 'Usuario', unique = True)
    name = models.CharField(max_length = 100, verbose_name = 'Alias', unique = True)
    description = models.TextField(verbose_name= 'description', null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "administrador quetzi"
        verbose_name_plural = "administradores quetzi"
        ordering = ['-created']

    def __str__(self):
        return self.name

