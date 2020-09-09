from django.shortcuts import render, redirect
from django.views.generic import ListView

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from.models import Author
from .forms import CreateUserForm
from .decorators import unauthenticated_user


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            Author.objects.create(user = user)
            messages.success(request, f'Account was created for {username}')
            return redirect('login')

    context = {'form':form}
    return render(request, 'mainapp/register.html', context)


@unauthenticated_user
def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username , password = password)

        if user is not None :
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request, 'username or password is incorrect')
            return render(request, 'mainapp/login.html', context)

    return render(request, 'mainapp/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
