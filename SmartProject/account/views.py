from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def doclogin(request):

    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        #username = User.objects.get(email=email.lower()).username
        if (username[:2] == 'Dr'):
            check = True
        else:
            check = False
        if (check):
            user = auth.authenticate(username=username, password = password)
            if (user is not None):
                auth.login(request, user)
            #redirected to home page
                return redirect('/Doctor')
            else:
                messages.info(request, "Credentials incorrect")
                return redirect('doclogin')
        else:
            messages.info(request, "Doctor not found")
            return redirect('doclogin')

    else:
        return render(request, 'Doclogin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def patlogin(request):

    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password = password)
        if (user is not None):
            auth.login(request, user)
            #redirected to home page
            return redirect('/Patient/Home')
        else:
            messages.info(request, "Credentials incorrect")
            print("Credentials incorrect")
            return redirect('patlogin')

    else:
        return render(request, 'PatSignIn.html')

def patsignup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        cond1 = cond2 = False
        if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                print('Username exists')
                cond1 = True
        
        if (password1!=password2):
            messages.info(request, 'Password not matching')
            print('Password not matching')
            cond2 = True
        
        if (cond1 or cond2):
            return  render(request,'PatSignUp.html')

        else:
            user = User.objects.create_user(
                username = username, 
                password = password1, 
                email = email, 
                first_name = first_name, 
                last_name = last_name
            )
            user.save()
            print('User created')
            return redirect('/account/Patlogin')
        
        
    else:
        return  render(request,'PatSignUp.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def storesignup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        cond1 = cond2 = False
        if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                print('Username exists')
                cond1 = True
        
        if (password1!=password2):
            messages.info(request, 'Password not matching')
            print('Password not matching')
            cond2 = True
        
        if (cond1 or cond2):
            return  render(request,'StoreSignUp.html')

        else:
            user = User.objects.create_user(
                username = username, 
                password = password1, 
                email = email, 
                first_name = first_name, 
                last_name = last_name
            )
            user.save()
            print('User created')
            return redirect('/account/Storelogin')
        
        
    else:
        return  render(request,'StoreSignUp.html')

def storelogin(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password = password)
        if (user is not None):
            auth.login(request, user)
            #redirected to home page
            return redirect('/Store/Home')
        else:
            messages.info(request, "Credentials incorrect")
            print("Credentials incorrect")
            return redirect('Storelogin')

    else:
        return render(request, 'Storelogin.html')
