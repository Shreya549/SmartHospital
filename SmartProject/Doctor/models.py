from django.db import models

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
