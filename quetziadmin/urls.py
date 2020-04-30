"""quetziadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.views.generic import RedirectView
from qtadmin.urls import qtadmin_patterns
from business.urls import business_patterns
from project.urls import project_patterns

urlpatterns = [
    path('', RedirectView.as_view(url = reverse_lazy('login'), permanent = False)),
    path('admin/', admin.site.urls),
    path('business/', include(business_patterns)),
    path('quetziadmin/', include(qtadmin_patterns)),
    path('project/', include(project_patterns)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

