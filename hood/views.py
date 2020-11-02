from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Neighborhood, Business
from .forms import CreateNeighborhoodForm


def index(request):
    return render(request, 'hood/index.html')


def home(request):
    return render(request, 'hood/home.html')


class PostListView(ListView):
    model = Post
    template_name = 'hood/home.html'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['businesses'] = Business.objects.all()
        context['total_businesses'] = Business.objects.all().count()
        context['total_neighborhoods'] = Neighborhood.objects.all().count()

        return context


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def display_hood(request):
    neighborhoods = Neighborhood.objects.all()
    return render(request, 'users/hood.html', {'hoods': neighborhoods})


def create_hood(request):
    form = CreateNeighborhoodForm()
    if request.method == 'POST':
        form = CreateNeighborhoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('neighborhood')

    context = {'form': form}
    return render(request, 'users/create_hood.html', context)


def update_hood(request, pk):
    hood = Neighborhood.objects.get(id=pk)
    form = CreateNeighborhoodForm(instance=hood)
    if request.method == 'POST':
        form = CreateNeighborhoodForm(request.POST, instance=hood)
        if form.is_valid():
            form.save()
            return redirect('neighborhood')
    context = {'form': form}
    return render(request, 'users/create_hood.html', context)


def delete_hood(request, pk):
    hood = Neighborhood.objects.get(id=pk)
    if request.method == 'POST':
        hood.delete()
        return redirect('neighborhood')
    context = {'item': hood}
    return render(request, 'users/delete.html', context)


def search(request):
    return render(request, 'users/search.html')


class SearchListView(ListView):
    model = Business
    template_name = 'users/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = self.request.GET.get('q')
        context['business'] = Business.objects.filter(
            business_name__icontains=query)
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Business.objects.filter(business_name__icontains=query)
        return object_list
