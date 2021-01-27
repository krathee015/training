from django.contrib import admin
from django.urls import path
from gitapp import views

urlpatterns = [
    
     path('git/', views.github,name = 'github'),

]