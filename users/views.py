from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, AdminRegisterForm
from hood.decorators import unauthenticate_user
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate


@unauthenticate_user
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='users')
            user.groups.add(group)

            messages.success(request, f'Account created successfully!')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


@unauthenticate_user
def admin_register(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='admin')
            user.groups.add(group)

            messages.success(request, f'Account created successfully!')
            return redirect('login')
    else:
        form = AdminRegisterForm()

    return render(request, 'registration/admin_register.html', {'form': form})


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info('Username or Password Incorrect')
    context = {}
    return render(request, 'registration/admin_login.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        user_update = UserUpdateForm(request.POST, instance=request.user)
        profile_update = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_update.is_valid() and profile_update.is_valid():
            user_update.save()
            profile_update.save()
            messages.success(
                request, f'Your account has been updated successfully!')
            return redirect('homepage')
    else:
        user_update = UserUpdateForm(instance=request.user)
        profile_update = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_update': user_update,
        'profile_update': profile_update,
    }
    return render(request, 'users/profile.html', context)
