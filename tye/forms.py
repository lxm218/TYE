from django import forms
from django.contrib.auth.models import User

from .models import Student



class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','school','state','country','grade']




