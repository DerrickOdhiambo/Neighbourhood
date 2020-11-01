from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


def index(request):
    return render(request, 'hood/index.html')


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'hood/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'hood/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
