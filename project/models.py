from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 
from qtadmin.models import QuetziAdmin
from business.models import Business
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length = 100)
    business = models.OneToOneField(Business, on_delete=models.CASCADE, verbose_name = 'Empresa')
    boss = models.ForeignKey(QuetziAdmin, on_delete=models.CASCADE, related_name = 'get_boss', verbose_name = 'Jefe del Proyecto')
    members = models.ManyToManyField(QuetziAdmin, verbose_name = 'Integrantes', related_name= 'get_p_members')
    description = models.TextField(verbose_name='Descripción')
    progress = models.PositiveIntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name = 'Porcentaje')
    initialDate = models.DateField(default = timezone.now, verbose_name='Fecha de inicio')
    finalDate = models.DateField(verbose_name= 'Fecha estimada de finalización')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Homework(models.Model):
    name = models.CharField(max_length=100, )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name = 'Tarea')
    members = models.ManyToManyField(QuetziAdmin, verbose_name = 'Integrantes', related_name= 'get_hw_members')
    description = models.TextField(verbose_name='Descripción')
    initialDate = models.DateField(default = timezone.now, verbose_name='Fecha de inicio')
    finalDate = models.DateField(verbose_name= 'Fecha estimada de finalización')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "tarea"
        verbose_name_plural = "tareas"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Report(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name = 'Proyecto')
    title = models.CharField(max_length = 100, verbose_name = 'Título')
    content = models.TextField(verbose_name='Contenido')