from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.control_panel, name='control_panel'),
    path('update_message/', views.update_message, name='update_message'),
    path('get_message/', views.get_message, name='get_message'),
    path('display/', views.display, name='display'),
    path('control_panel/', views.control_panel, name='control_panel'),
    path('register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += staticfiles_urlpatterns()