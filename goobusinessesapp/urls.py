from django.contrib import admin
from django.urls import path
from goobusinessesapp import views

urlpatterns = [
    # path("", views.index, name='home'),

    # path("", views.intro, name="intro"),

    path("", views.service, name="service"),
    path("one", views.one, name="one"),
    path("two", views.two, name="two"),
    path("three", views.three, name="three"),
    path("four", views.four, name="four"),
    path("five", views.five, name="five"),
   

 
    


    
]
