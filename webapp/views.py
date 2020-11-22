from django.shortcuts import render
from webapp.forms import UserForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from webapp.models import *
from django.contrib.auth.decorators import login_required
# Create your views


def home_view(request):
    return render(request, 'index.html')


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/menu')
    else:
         if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'You are Login Successfully')
                return HttpResponseRedirect('/menu')
         return render(request, 'loginpage.html')


def signup_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/menu')
    else:
        form = UserForm()
        if request.method == 'POST':
            form= UserForm(request.POST)
            if form.is_valid():
                form.save()
                s = form.cleaned_data.get('username')
                messages.info(request, 'You are Register Successfully...!'+s)
                return HttpResponseRedirect('/login')
        return render(request, 'signup.html', {'form': form})


@login_required(login_url='/login')
def menu_view(request):
    return render(request, 'menu.html')


@login_required(login_url='/login')
def reservation_view(request):
    if request.method == 'POST':
        table = BookTable()
        table.Name = request.POST.get('name')
        table.People = request.POST.get('many')
        table.Task = request.POST.get('taskdatetime')
        table.save()
        messages.info(request, table.Name+' You Have Book Table on '+table.Task)
    return render(request, 'reservation.html')


def contact_view(request):
    if request.method == 'POST':
        ct = Contact()
        ct.Name = request.POST.get('name')
        ct.Email = request.POST.get('email')
        ct.Msg = request.POST.get('msg')
        ct.save()
        messages.info(request, ct.Name+' Thank You For Your Suggetion ')
    return render(request, 'contact.html')


def about_view(request):
    return render(request, 'about.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')