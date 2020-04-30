from django.db import models
from django.contrib.auth.admin import User
from cropperjs.models import CropperImageField
from uuid_upload_path import upload_to

# Create your models here.
class Business(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, verbose_name = 'Usuario', unique = True)
    business = models.CharField(max_length = 100, verbose_name = 'Nombre de la Empresa', unique = True, blank = False, null = False)
    description = models.TextField(verbose_name= 'Descripción', null = True, blank = True)
    image = CropperImageField(verbose_name='foto de perfil', upload_to=upload_to, null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "empresa"
        verbose_name_plural = "empresas"
        ordering = ['-created']

    def __str__(self):
        return self.business