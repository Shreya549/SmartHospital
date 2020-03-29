from django.urls import path
from . import views

urlpatterns = [
    path('Doclogin', views.doclogin, name = 'doclogin'),
    path('Doclogout', views.doclogout, name = 'doclogout')
]