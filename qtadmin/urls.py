from django.urls import path
from .views import QtAdminHomeView, QtProfileConfig
qtadmin_patterns = ([
    path('home/', QtAdminHomeView.as_view(), name = 'home'),
    path('profile/', QtProfileConfig.as_view(), name = 'profile'),
], 'quetziadmin')