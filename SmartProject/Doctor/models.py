from django.db import models

# Create your models here.

class DoctorInfo(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    spec = models.TextField()
    timings = models.TextField()
    img = models.ImageField(upload_to  = 'pics')
    qualif = models.TextField()
