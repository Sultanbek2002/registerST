from django.shortcuts import render, redirect
from .forms import StudentForm
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.
def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'useaccounts/login.html')


def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'useaccounts/register.html', {'form': StudentForm})


def logout(request):
    auth.logout(request)
    return redirect('home')
