from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from my_app.models import NotesList


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('Login Error'))
            return redirect('login')
    elif request.method == 'GET':
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_user')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if not check_if_user_exists(email):
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()
            create_list_for_new_user(user)

            return redirect('login_user')
        else:
            return redirect('signup_user')

    if request.method == 'GET':
       return render(request, 'signup.html')

def check_if_user_exists(email):
    return User.objects.filter(email=email).exists()

def create_list_for_new_user(user):
    NotesList.objects.create(user=user, list_name='default')