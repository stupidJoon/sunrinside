from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            User.objects.create_user(username=request.POST["id"], password=request.POST["password1"])
            return redirect('signin')
        else:
            return render(request, 'signup.html')

def signin(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST["id"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            return render(request, 'login.html')

def signout(request):
    auth.logout(request)
    return redirect('index')