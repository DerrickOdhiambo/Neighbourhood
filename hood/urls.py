from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, SearchListView


urlpatterns = [
    path('', views.index, name='landing-page'),
    path('home/', PostListView.as_view(), name='homepage'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('neighborhood/', views.display_hood, name='neighborhood'),
    path('search/', views.search, name='search'),
    path('search/search_business/',
         SearchListView.as_view(), name='search-business'),
    path('create_business/', views.create_business, name='create_business'),
    path('create/', views.create_hood, name='create_hood'),
    path('update/<int:pk>', views.update_hood, name='update_hood'),
    path('delete/<int:pk>', views.delete_hood, name='delete_hood'),
]
