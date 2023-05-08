from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #auth
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "YOU have been loggged in!")
            return redirect('home')
        else:
            messages.success(request, "I have an error logging, please try aigain")
            return redirect('home')
    else:
        return render(request, "home.html", {})


def log_out(request):
    logout(request)
    messages.success(request, "YOU Have been logout successfully")
    return redirect('home')

def register_user(request):
    return render(request, "register.html", {})