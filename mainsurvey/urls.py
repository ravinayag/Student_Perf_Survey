from django.contrib import admin
from django.urls import path
from . import views
from .forms import ContactForm1,ContactForm2

app_name = 'mainsurvey'

urlpatterns = [
    path('mainsurvey/',views.page2,name = 'page2'),
]
