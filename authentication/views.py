'''This import is used to import the render function'''
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import Signup, Login

# Create your views here.


def home(request):
    '''This function is used to render the home page'''
    data = {
        'user': request.user  # Pass the user object to the template context
    }
    return render(request, 'index.html', data)


def register(request):
    '''This function is used to render the signup/registeration page'''
    signup_form = Signup()
    if request.method == 'POST':
        signup_form = Signup(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('login')
    data = {
        'signup_form': signup_form
    }
    return render(request, 'register.html', data)


def user_login(request):
    '''This function is used to render the login page'''
    login_form = Login()
    if request.method == 'POST':
        login_form = Login(request, data=request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')

    data = {
        'login_form': login_form
    }
    return render(request, 'login.html', data)


def user_logout(request):
    '''This function is used to render the dashboard page'''
    logout(request)
    messages.warning(request, 'You have been logged out.')
    return redirect('home')


def dashboard(request):
    '''This function is used to render the dashboard page'''
    return render(request, 'dashboard.html')
