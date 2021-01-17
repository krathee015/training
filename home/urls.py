from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.index,name = 'index'),
    path('about/',views.about,name ='about'),
    path('projectform/',views.projectform,name ='pf'),
    path('projectform/submit/',views.submitmessage,name ='sm'),
    path('userform/', views.userview,name ="uf"),
    

]