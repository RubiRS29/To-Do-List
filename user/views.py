from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import LoginForm, RegisterForm

# Create your views here.

def register(request):
    form = RegisterForm(request.POST )

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')

    return render(request , 'user/register.html' , {
        'form': form
    })

def login_view(request):

    form = LoginForm( request.POST )

    if request.method == 'POST' :

        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email, password)

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('../ToDoList')
        else:
            messages.error(request , "Email or password incorret")

    return render(request , 'user/login.html' , {
        'form': form
    })

def logout_view(request):
    logout(request)
    messages.success(request , "Logout successful")
    return redirect('index')

