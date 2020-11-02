from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class RegisterForm(UserCreationForm):
    username = forms.CharField(label=False, max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username...'}))
    first_name = forms.CharField(label=False, max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name...'}))
    last_name = forms.CharField(label=False, max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name...'}))
    email = forms.EmailField(label=False, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email..'}))
    password1 = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Password..."}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Confirm Password..."}))

    class Meta:
        model = User
        fields = ['username', 'email',
                  'first_name', 'last_name', 'password1', 'password2']


class AdminRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email',
                  'first_name', 'last_name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'id_number', 'neighborhood']
