from django.urls import path
from . import views

urlpatterns = [
    # Core App Views
    path('', views.dashboard, name='dashboard'),
    path('add-match/', views.add_match, name='add_match'),
    path('add-workout/', views.add_workout, name='add_workout'),
    
    # Custom Registration View
    path('register/', views.register, name='register'), 
    
    # Login and Logout paths are handled exclusively by fitness_tracker/urls.py
]