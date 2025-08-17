from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User


def home(request):
    return render(request, 'html/selection.html')

def index(request):
    return render(request, 'html/index.html')

@login_required(login_url='login')
def books(request):
    return render(request, 'html/books.html')

def returnn(request):
    return render(request, 'html/return.html')

def contact(request):
    return render(request,'html/contact.html')

def admin_custom(request):
    return render(request,'html/admin_custom.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:  # allow only admin/staff users
                auth_login(request, user)
                return redirect('admin_custom')  # or wherever you want
            else:
                messages.error(request, 'Access denied. Not an admin user.')
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'html/login.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                messages.error(request,'Access Denied')
                return redirect('user_login')
            else:
                auth_login(request, user)
                return redirect('index')  # or wherever you want
        else:
            return render(request, 'html/login.html', {
                'error': 'Invalid username or password',
                'username': username
            })
    return render(request, 'html/login.html')


def logout_view(request):
    auth_logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')

# Fake register view (you should implement actual user creation)
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if(password1!=password2):
            messages.error(request,"Passwords don't match")
            return redirect('register')
        if(User.objects.filter(username=username).exists()):
            messages.error(request,"username already exist")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')
        user=User.objects.create_user(username=username,email=email,password=password1)
        user.save()
        messages.success(request,"Account created successfully. Please Log in.")
        return redirect('user_login')
    return render(request,'html/register.html')
