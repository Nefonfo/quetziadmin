from django.contrib import admin
from .models import QuetziAdmin
# Register your models here.

class QuetziAdminAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(QuetziAdmin, QuetziAdminAdmin)