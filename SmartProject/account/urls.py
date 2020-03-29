from django.urls import path
from . import views

urlpatterns = [
    path('Doclogin', views.doclogin, name = 'doclogin')
]