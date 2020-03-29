from django.urls import path
from . import views

urlpatterns = [
    path('Doclogin', views.doclogin, name = 'doclogin'),
    path('Doclogout', views.doclogout, name = 'doclogout'),
    path('Patlogin', views.patlogin, name = 'patlogin'),
    path('PatSignup', views.patsignup, name = 'patsignup')
]