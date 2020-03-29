from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def Home(request):
    #user not signed in
    if (not User.is_authenticated):
        return redirect('/account/login')
    #user signed in
    else:
        return redirect('/Doctor/Home')
        