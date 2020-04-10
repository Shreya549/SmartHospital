from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Appointment
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.

def Home(request):
    return render(request, 'DocHome.html')

@login_required
def FindPatients(request):
    if request.method == 'POST':
        username = request.POST['username']
        try: 
            doc_username = Appointment.objects.get(username = username, treated = False).doctor_username
        except ObjectDoesNotExist:
            doc_username = None
        if (doc_username is not None):
            current_doctor = request.user.get_username()
            if (current_doctor == doc_username):
                return redirect('/Doctor/TreatPatient')
            else:
               messages.info(request,'Patient not registered under you!')
               return redirect('/Doctor/FindPatients')
        else:
            messages.info(request, 'Patient has no active appointment!')
            return redirect('/Doctor/FindPatients')
    else:
        return render(request, 'DocFindPatients.html')

@login_required
def TreatPatient(request):
    return render(request, 'Doctreatpatient.html')
    