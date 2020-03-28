from django.contrib import admin
from .models import Business
# Register your models here.

class BusinessAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Business, BusinessAdmin)