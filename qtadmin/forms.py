from django import forms
from .models import QuetziAdmin
from cropperjs.widgets import ClearableFileInput

class QtAdminEditProfileCrop(forms.ModelForm):
    class Meta:
        model = QuetziAdmin
        fields = ['image', 'name', 'description']
        widgets = {
            'image': ClearableFileInput(),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 40})
        }