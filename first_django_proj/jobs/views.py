import random

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from django.views.generic import CreateView

from first_django_proj import settings
from jobs.models import Person


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


class MyUserCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('username', 'email')

class RegisterView(CreateView):
    model = Person
    form_class = MyUserCreationForm

    def form_valid(self, form):
        code = str(random.randint(100000, 999999))
        form.cleaned_data['code'] = code
        send_mail("Registration confirmation code", code, settings.EMAIL_HOST_USER)
        form.save()
        user = User.objects.create_user(username=form.cleaned_data['email'], email=form.cleaned_data['email'], is_active=False)
        user.save()
        return super(RegisterView, self).form_valid(form)


class RegistrationCodeView(View):
    def post(self, request):
        email = request.POST['email']
        person = Person.objects.get(email=email)
        code = request.POST['code']
        if code == person.code:
            person.user.is_active = True
            person.user.save()
            messages.success(request, 'You are now logged in.')
            return redirect('/jobs/login/')