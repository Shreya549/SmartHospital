from django.urls import path
from . import views

urlpatterns = [
    path('Home', views.Home, name = 'Home'),
    path('BookAppointment', views.BookAppointment, name = 'BookAppointment')
]