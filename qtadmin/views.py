from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from .custom_mixin import IsQtAdminRequiredMixin
# Create your views here.

@method_decorator(login_required, name = 'dispatch')
class QtAdminHomeView(IsQtAdminRequiredMixin, TemplateView):
    template_name = "qtadmin/home.html"