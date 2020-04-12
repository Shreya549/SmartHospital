from django.urls import path
from . import views

urlpatterns = [
    path('Doclogin', views.doclogin, name = 'doclogin'),
    path('logout', views.logout, name = 'logout'),
    path('Patlogin', views.patlogin, name = 'patlogin'),
    path('PatSignup', views.patsignup, name = 'patsignup'),
    path('Storelogin', views.storelogin, name = 'storelogin'),
    path('Storesignup', views.storesignup, name = 'storesignup')
]