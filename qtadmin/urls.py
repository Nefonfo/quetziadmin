from django.urls import path
from .views import QtAdminHomeView
qtadmin_patterns = ([
    path('home/', QtAdminHomeView.as_view(), name = 'home')
], 'quetziadmin')