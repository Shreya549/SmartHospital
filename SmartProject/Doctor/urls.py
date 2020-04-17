from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = 'Home'),
    path('FindPatients', views.FindPatients, name = 'FindPatients'),
    path('TreatPatient', views.TreatPatient, name = 'TreatPatient'),
    path('ViewHistory', views.ViewHistory, name = 'ViewHistory')
]