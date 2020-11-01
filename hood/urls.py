from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView


urlpatterns = [
    path('', views.index, name='landing-page'),
    path('home/', PostListView.as_view(), name='homepage'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('neighborhood/', views.display_hood, name='neighborhood'),
    path('neighborhood/create/', views.create_hood, name='create_hood'),
]
