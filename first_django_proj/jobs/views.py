from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            request.session['last_login'] = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
            login(request, user)
            messages.success(request, 'You are now logged in.')
            print(request.session.items())
            response = redirect(request.GET.get('next','index'))
            response.set_cookie('last_login', timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
            return response
        else:
            return HttpResponse("login failed")

@login_required(login_url="/jobs/login/")
def logout_view(request):
    if request.method == 'GET':
        return render(request, 'logout.html')
    elif request.method == 'POST':
        logout(request)
        return HttpResponse("logged out")
