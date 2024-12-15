from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .form import LoginForm

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid login details')
    return render(request, 'login.html', {'form': LoginForm})
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful signup
            return redirect('index.html')  # Redirect to home page after sign up
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.info(request, 'You have been logged out!!')
    return redirect('/')
