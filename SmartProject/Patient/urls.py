from django.urls import path
from . import views

urlpatterns = [
    path('Home', views.Home, name = 'Home'),
    path('BookAppointment', views.BookAppointment, name = 'BookAppointment'),
    path('PendingAppointments', views.PendingAppointments, name = 'PendingAppointments'),
    path('PreviousReports', views.PreviousReports, name = 'PreviousReports')
]
