from django.shortcuts import render , redirect, get_object_or_404
from .forms import ProjectForm, UserForm,BookForm
from .models import Books

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
    book = Books.objects.all()
    context = {"object_list": book}
    return render(request,"book/book.html",context)

def book_view(request, pk, template_name='book/book_detail.html'):
    book= get_object_or_404(Books, pk=pk)
    return render(request, template_name, {'object':book})

def book_create(request, template_name='book/book_create.html'):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form':form})

def book_edit(request, pk, template_name='book/book_create.html'):
    book= get_object_or_404(Books, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form':form})

def book_delete(request, pk, template_name='book/book_delete.html'):
    book = get_object_or_404(Books, pk=pk)
    if request.method=='POST':
        book.delete()
        return redirect('book_list')
    return render(request, template_name, {'object':book})




