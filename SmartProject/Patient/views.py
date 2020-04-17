from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from Doctor.models import Appointment
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from datetime import datetime

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
            treated = False,
            date_booked = datetime.today().strftime('%Y-%m-%d')
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
        date_booked = Appointment.objects.filter(username = username, treated = False).values("date_booked")
        appoint = []
        entry = ()
        doct = []
        num = 0
        for i in doctor:
            doct.append(i['doctor_username'])
        
        prob = []
        for i in problem:
            prob.append(i['problem'])
        
        booking_date = []
        for date in date_booked:
            booking_date.append(date['date_booked'])
        
        for i in range (len(doct)):
            entry = (doct[i], prob[i], booking_date[i])
            appoint.append(entry)

        num = len(doct)
        return render(request, 'PatPendAppoint.html', {"pending_appoints" : appoint, "num_of_reports" : num})
        
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
        date_booked = Appointment.objects.filter(username = username, treated = True).values("date_booked")
        date_treated = Appointment.objects.filter(username = username, treated = True).values("date_treated")

        comp_report = []
        doc = []
        prob = []
        rem = []
        med = []
        entry = ()
        book = []
        treat = []

        for i in doctor:
            doc.append(i["doctor_username"])
        for i in problem:
            prob.append(i["problem"])
        for i in remark:
            rem.append(i["remark"])
        for i in medicines:
            med.append(i["medicines"])
        for i in date_booked:
            book.append(i["date_booked"])
        for i in date_treated:
            treat.append(i["date_treated"])
        
        num = len(prob)

        for i in range (len(doc)-1, -1, -1):
            entry = (doc[i], prob[i], book[i], rem[i], med[i], treat[i])
            comp_report.append(entry)
        return render(request, 'PatPrevReports.html', {"prev_reports" : comp_report, 'number' : num})
        
    except ObjectDoesNotExist:
        print("Helo")
        messages.info(request, "You do not have any previous reports")
        return render(request, "PatPrevReports.html")
    
    