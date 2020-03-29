from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def doclogin(request):

    if(request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email.lower()).username
        if (username[:2] == 'Dr'):
            check = True
        else:
            check = False
        if (check):
            user = auth.authenticate(username=username, password = password)
        if (user is not None):
            auth.login(request, user)
            #redirected to home page
            return render(request, 'DocHome.html')
        else:
            messages.info(request, "Credentials incorrect")
            print("Credentials incorrect")
            return redirect('doclogin')

    else:
        return render(request, 'Doclogin.html')

def doclogout(request):
    auth.logout(request)
    return redirect('/')

