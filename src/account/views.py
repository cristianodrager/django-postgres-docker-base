from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def account_profile(request):
    return render(request, 'profile.html')

def account_signup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # Inicia sessão do usuário
        login(request, user)
        next_url = request.GET.get('next') or 'account-profile'
        return redirect(next_url)
    else:
        return redirect('account-login')
    

def account_login(request):
    return render(request, 'login.html')

def account_logout(request):
    logout(request)
    return redirect('account-login')