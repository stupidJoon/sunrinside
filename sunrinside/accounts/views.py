from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse

def signup(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
        auth.login(request, user)
        return redirect('')
    else:
        return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')