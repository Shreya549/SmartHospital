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
        global username
        username = request.POST['username']
        try: 
            active_appoint = Appointment.objects.filter(username = username, treated = False).values('doctor_username')
        except ObjectDoesNotExist:
            active_appointment = None

        if (active_appoint is not None):
            global current_doctor
            current_doctor = request.user.get_username()
            doctor_found = False
            for i in active_appoint:
                if (i['doctor_username'] == current_doctor):
                    doctor_found = True
            if (doctor_found):
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
    problem = Appointment.objects.filter(username = username, treated = False, doctor_username = current_doctor ).values('problem')
    probs = []
    for i in problem:
        probs.append(i['problem'])
    if request.method == 'POST':
        remark = request.POST["remark"]
        medicine = request.POST["medicine"]
        entry = Appointment.objects.get(username = username, treated = False)
        entry.remark = remark
        entry.medicines = medicine
        entry.treated = True
        entry.save()

        return render (request, 'Doctreatpatient.html')
    return render(request, 'Doctreatpatient.html', {'name': username, 'problem': probs})
    