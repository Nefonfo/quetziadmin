from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from .custom_mixin import IsQtAdminRequiredMixin
from project.models import Project, Homework
from qtadmin.models import QuetziAdmin
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