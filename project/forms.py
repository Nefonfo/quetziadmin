from django import forms
from .models import Project
from business.models import Business
from qtadmin.models import QuetziAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'business', 'boss', 'description', 'initialDate', 'finalDate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'boss': forms.Select(attrs={'class': 'form-control'}),
            'business': forms.Select(attrs={'class': 'form-control'}),
            'members': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'initialDate': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
            'finalDate': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
        }