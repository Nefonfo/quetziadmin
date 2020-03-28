from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .custom_mixin import IsBusinessRequiredMixin
# Create your views here.

@method_decorator(login_required, name = 'dispatch')
class BusinessHomeView(IsBusinessRequiredMixin, TemplateView):
    template_name = "business/home.html"
    
   
    