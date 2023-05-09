from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.


def home(request):
    records = Record.objects.all()
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # auth
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "YOU have been loggged in!")
            return redirect('home')
        else:
            messages.success(
                request, "I have an error logging, please try aigain")
            return redirect('home')
    else:
        return render(request, "home.html", {'records': records})


def log_out(request):
    logout(request)
    messages.success(request, "YOU Have been logout successfully")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully Register")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, "register.html", {'form': form})

    return render(request, "register.html", {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, "record.html", {'customer_record': customer_record})
    else:
        messages.success(request, "You login on view")
        return redirect('home')


def delete_customer(request, pk):
    if request.user.is_authenticated:
        delet_it = Record.objects.get(id=pk)
        delet_it.delete()
        messages.success(request, "Records deleted succcessfully!")
        return redirect('home')
    else:
        messages.success(request, "you must be Logged in to do that...")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "record Added")
                return redirect('home')
        return render(request, "add_record.html", {'form': form})
    else:
        messages.success(request, "you must be Logged in to do that...")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance = current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "record update")
            return redirect('home')
        return render(request, "update_record.html", {'form': form})
    else:
        messages.success(request, "you must be Logged in to do that...")
        return redirect('home')