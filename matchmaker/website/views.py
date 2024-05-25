from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .forms import SignUpForm, CreateGroupForm

def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        if request.user.is_authenticated:
            return render(request, 'home.html')
        else:
            return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
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
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        context = {
            'form':form,
            'form_name':'Register'
        }
        return render(request, 'form.html', context)


def create_pickup_group(request):
    if request.method == 'POST':
        new_group, created = Group.objects.get_or_create(name=request.POST.get('group_name'))
        print(new_group)
        request.user.groups.add(new_group)
        return redirect('home')
    else:
        form = CreateGroupForm()
        context = {
            'form':form,
            'form_name':'Create Group'
        }
        return render(request, 'form.html', context)
