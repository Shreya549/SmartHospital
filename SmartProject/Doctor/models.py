from django.db import models
import datetime

# Create your models here.

class DoctorInfo(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    spec = models.TextField()
    timings = models.TextField()
    img = models.ImageField(upload_to  = 'pics')
    qualif = models.TextField()


class Appointment(models.Model):
    username = models.CharField(max_length = 100)
    doctor_username = models.CharField(max_length = 100)
    problem = models.TextField()
    remark = models.TextField()
    medicines = models.TextField()
    treated = models.BooleanField()
    date_booked = models.DateField(default = datetime.date.today)
    date_treated = models.DateField(default = datetime.date.today)
