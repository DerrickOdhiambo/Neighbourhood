from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='landing-page'),
    path('home/', views.home, name='homepage'),
]
