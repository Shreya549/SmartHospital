from django.urls import path
from . import views

urlpatterns = [
    path('', views.ind, name = 'ind'),
    path('Home', views.home, name = 'home')
]