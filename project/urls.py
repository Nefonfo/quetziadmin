from django.urls import path
from .views import ProjectCreateView
project_patterns = ([
    path('create/', ProjectCreateView.as_view(), name = 'create')
], 'project')