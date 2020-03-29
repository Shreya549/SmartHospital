from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def doclogin(request):

    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password, is_staff = True )
        if (user is not None):
            auth.login(request, user)
            #redirected to home page
            return render(request, 'DocHome.html')
        else:
            messages.info(request, "Credentials incorrect")
            return redirect('doclogin')

    else:
        return render(request, 'Doclogin.html')

def doclogout(request):
    auth.logout(request)
    return redirect('/')

