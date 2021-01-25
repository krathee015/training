from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.index,name = 'index'),
    path('about/',views.about,name ='about'),
    path('projectform/',views.projectform,name ='pf'),
    path('projectform/submit/',views.submitmessage,name ='sm'),
    path('userform/', views.userview,name ="uf"),
    path('booklist/',views.book_list,name ="BL"), 
    path('bookview/<int:pk>',views.book_view,name ="BV"), 
    path('bookedit/<int:pk>',views.book_edit,name ="BE"), 
    path('bookdel/<int:pk>',views.book_delete,name ="BD"), 
    path('bookcreate/',views.book_create,name ="BC"), 
    path('bookAPI/',views.Book_Serializer_View.as_view(),name ="BAPI"),
]