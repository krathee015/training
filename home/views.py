from django.shortcuts import render
from .forms import ProjectForm, UserForm, BookForm

# Create your views here.

from django.http import HttpResponse

def index(request):
    context = {'tag_var':'tag_var'}
    return render(request,"home/demo.html",context)
    

def about(request):
    return HttpResponse("It is about page of Django project")

def projectform(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request,"home/project.html",context)

def submitmessage(request):
    return HttpResponse("Data is submitted")

# to save the model form in the backend which is admin
def userview(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save() 
        form = UserForm()
    context = {'form':form}
    return render(request,"home/userform.html",context)

# To view the book as a list

def book_list(request):
    book = BookForm.object.all()
    context = {"object_list":book}
    return render(request,"home/book.html",context)




