from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
## PUT ALL MIXINS OF BUSINESS HERE
class IsBusinessRequiredMixin(object):
     def dispatch(self, request, *args, **kwargs):
            try:
                data = request.user.business
            except:
                return redirect(reverse_lazy('login'))
            return super(IsBusinessRequiredMixin, self).dispatch(request, *args, **kwargs)