from django.urls import path
from .views import BusinessHomeView
business_patterns = ([
    path('home/', BusinessHomeView.as_view(), name = 'home')
], 'business')