from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('admin_register/', views.admin_register, name='admin_register'),
    path('admin_login/', views.admin_login, name='admin_login'),
    # path('profile/', views.profile, name='profile'),
    # path('login/', UserRegisterView.as_view(), name='login'),
]
