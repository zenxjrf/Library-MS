from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def loginview(request):
    if request.method == 'POST':
        users = authenticate(username=request.POST.get('login'), password=request.POST.get('parol'))
        if users is None:
            return redirect("/")
        login(request,users)
        return redirect('/home/')
    return render(request,'login.html')

def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect('/login/')

def logoutview(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == "POST":
        User.objects.create_user(
            username = request.POST.get("l"),
            password = request.POST.get('p')
        )
        return redirect('/home/')
    return render(request,'register.html')