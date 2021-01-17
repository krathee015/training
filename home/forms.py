from django import forms
from django.db.models.base import Model
from .models import User

class ProjectForm(forms.Form):
    ProjectName = forms.CharField(label = "Project Name", max_length = 10)
    ProjectDetails = forms.CharField(label = "Project Details", max_length = 100)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"