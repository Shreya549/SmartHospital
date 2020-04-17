from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Appointment
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from datetime import datetime

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
            active_appoint = None

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
    pat_name = (User.objects.filter(username = username).values("first_name"))
    patient_name = pat_name[0]['first_name']
    probs = []
    for i in problem:
        probs.append(i['problem'])
    if request.method == 'POST':
        remark = (request.POST["remark"])
        medicine = request.POST["medicine"]
        entry = Appointment.objects.filter(username = username, treated = False)
        for i in entry:
            i.remark = remark
            i.medicines = medicine
            i.treated = True
            i.date_treated = datetime.today().strftime('%Y-%m-%d')
            i.save()

        return redirect('/Doctor/FindPatients')
    return render(request, 'Doctreatpatient.html', {'name': username, 'problem': probs, 'Patient_Name' : patient_name})

def ViewHistory(request):

    try:
        pat_name = (User.objects.filter(username = username).values("first_name"))
        patient_name = pat_name[0]['first_name']
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
        return render(request, 'DocViewHistory.html', {"prev_reports" : comp_report, 'number' : num, 'Patient_Name' : patient_name})
        
    except ObjectDoesNotExist:
        messages.info(request, "You do not have any previous reports")
        return render(request, "DocViewHistory.html")
    