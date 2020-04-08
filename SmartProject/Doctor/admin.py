from django.contrib import admin
from .models import Appointment, DoctorInfo

# Register your models here.

admin.site.register(Appointment)
admin.site.register(DoctorInfo)