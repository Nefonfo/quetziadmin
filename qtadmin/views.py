from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic import UpdateView
from django.http import JsonResponse
from django.urls import reverse_lazy
from project.models import Project, Homework
from .custom_mixin import IsQtAdminRequiredMixin
from qtadmin.models import QuetziAdmin
from .forms import QtAdminEditProfileCrop
# Create your views here.

@method_decorator(login_required, name = 'dispatch')
class QtAdminHomeView(IsQtAdminRequiredMixin, TemplateView):
    template_name = "qtadmin/home.html"

    def get(self, request, *args, **kwargs):
        myprojects = None
        myHw = None
        myProfile = QuetziAdmin.objects.filter(user = request.user).first()
        if myProfile is not None:
            myprojects = Project.objects.filter(boss = myProfile)
            myHw = Homework.objects.filter(members__user = request.user)
        return render(request, self.template_name, {'projects': myprojects, 'homeworks': myHw})

class QtProfileConfig(UpdateView):
    model = QuetziAdmin
    form_class = QtAdminEditProfileCrop
    template_name="qtadmin/user_form.html"
    success_url = reverse_lazy('quetziadmin:profile')

    def get_object(self, queryset=None):
        return QuetziAdmin.objects.get(user = self.request.user)

