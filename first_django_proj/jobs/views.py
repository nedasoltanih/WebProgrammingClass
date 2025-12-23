from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.GET['next'])
        else:
            return HttpResponse("login failed")

@login_required(login_url="/jobs/login/")
def logout_view(request):
    if request.method == 'GET':
        return render(request, 'logout.html')
    elif request.method == 'POST':
        logout(request)
        return HttpResponse("logged out")
