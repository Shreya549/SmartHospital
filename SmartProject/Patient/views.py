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


def PendingAppointments(request):
    username = request.user.get_username()
    try:
        doctor = Appointment.objects.filter(username = username, treated = False).values("doctor_username")
        problem = Appointment.objects.filter(username = username, treated = False).values("problem")
        appoint = []
        entry = ()
        doct = []
        for i in doctor:
            doct.append(i['doctor_username'])
        prob = []
        for i in problem:
            prob.append(i['problem'])
        for i in range (len(doct), -1):
            entry = (doct[i], prob[i])
            appoint.append(entry)
            print(entry)
        return render(request, 'PatPendAppoint.html', {"pending_appoints" : appoint})
        
    except ObjectDoesNotExist:
        messages.info(request, "You do not have any pending appointments")
        return render(request, 'PatPendAppoint.html')


def PreviousReports(request):
    username = request.user.get_username()
    try:
        doctor = Appointment.objects.filter(username = username, treated = True).values("doctor_username")
        problem = Appointment.objects.filter(username = username, treated = True).values("problem")
        remark = Appointment.objects.filter(username = username, treated = True).values("remark")
        medicines = Appointment.objects.filter(username = username, treated = True).values("medicines")
        comp_report = []
        doc = []
        prob = []
        rem = []
        med = []
        entry = ()
        for i in doctor:
            doc.append(i["doctor_username"])
        for i in problem:
            prob.append(i["problem"])
        for i in remark:
            rem.append(i["remark"])
        for i in medicines:
            med.append(i["medicines"])
            
        for i in range (len(doc)):
            entry = (doc[i], prob[i], rem[i], med[i])
            comp_report.append(entry)
        return render(request, 'PatPrevReports.html', {"prev_reports" : comp_report})
        
    except ObjectDoesNotExist:
        print("Helo")
        messages.info(request, "You do not have any previous reports")
        return render(request, "PatPrevReports.html")
    
    