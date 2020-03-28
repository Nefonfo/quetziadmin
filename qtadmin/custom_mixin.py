from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
## PUT ALL MIXINS OF BUSINESS HERE
class IsQtAdminRequiredMixin(object):
     def dispatch(self, request, *args, **kwargs):
            try:
                data = request.user.quetziadmin
            except:
                return redirect(reverse_lazy('login'))
            return super(IsQtAdminRequiredMixin, self).dispatch(request, *args, **kwargs)