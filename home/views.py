from django.shortcuts import render
from .forms import ProjectForm, UserForm

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

def userview(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm()
    context = {'form':form}
    return render(request,"home/userform.html",context)



