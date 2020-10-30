from django.shortcuts import render
from django.views import generic


def index(request):
    return render(request, 'hood/index.html')


def home(request):
    return render(request, 'hood/home.html')
