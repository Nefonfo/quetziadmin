from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from qtadmin.models import QuetziAdmin
from business.models import Business

# Create your views here.
class ProfileView(UpdateView):
    model = QuetziAdmin
    template_name = 'registration/profile.html'
    fields = ['user', 'name']
    success_url = reverse_lazy('profile')
    def dispatch(self, request, *args, **kwargs):
        try:
            data = self.request.user.quetziadmin
        except:
            try:
                data = self.request.user.business
            except:
                return redirect(reverse_lazy('admin'))
            else:
                return redirect(reverse_lazy('business:home'))
        else:
            return redirect(reverse_lazy('quetziadmin:home'))

