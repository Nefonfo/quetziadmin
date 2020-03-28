from django.contrib import admin
from .models import Project, Homework
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    filter_horizontal = ('members',)

class ProjectMemberAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    

class HomeworkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    filter_horizontal = ('members',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Homework, HomeworkAdmin)