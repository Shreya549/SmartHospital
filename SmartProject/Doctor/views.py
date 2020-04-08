from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Appointment
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def Home(request):
    return render(request, 'DocHome.html')

def FindPatients(request):
    if request.method == 'POST':
        username = request.POST['username']
        try: 
            doc_username = Appointment.objects.get(username = username, treated = False).doctor_username
        except ObjectDoesNotExist:
            doc_username = None
        if (doc_username is not None):
            print(User.get_username())
        return redirect('/')
    else:
        return render(request, 'DocFindPatients.html')
    