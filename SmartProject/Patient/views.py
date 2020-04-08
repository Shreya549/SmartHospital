from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from Doctor.models import Appointment
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.


def Home(request):
    return render(request, 'PatHome.html')

@login_required
def BookAppointment(request):
    if request.method == 'POST':
        doc_username = request.POST['doc_username']
        current_patient = request.user.get_username()
        problem = request.POST['problem']
        
        if (User.objects.filter(username=doc_username).exists() and doc_username[:2] == 'Dr'):
            appointment = Appointment(
            username = current_patient, 
            doctor_username = doc_username,
            problem = problem,
            treated = False
            )
            appointment.save()
            return redirect('/Patient/Home')
        else:
            messages.info(request, 'Wrong Doctor Username. Please verify and try again')
            return redirect('/Patient/BookAppointment')
    else:
        return render(request, 'PatAppointment.html')