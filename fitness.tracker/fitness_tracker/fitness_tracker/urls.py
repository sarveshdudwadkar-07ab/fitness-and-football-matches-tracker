from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin Site
    path('admin/', admin.site.urls),

    # App-specific URLs (This now correctly includes the simple tracker/urls.py)
    path('', include('tracker.urls')), 
    
    # 🔑 FIX: Explicitly define the built-in login view
    path('accounts/login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    
    # 🔑 FIX: Explicitly define the built-in logout view (Requires POST)
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Include remaining built-in authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),
]