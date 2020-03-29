from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def ind(request):
    return redirect('/account/Patlogin')

def home(request):
    return render(request, 'PatHome.html')