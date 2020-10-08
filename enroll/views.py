from django.shortcuts import render
#from django.contrib.auth.decorators import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Student
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)


# Create your views here.
class StudentListView(LoginRequiredMixin,ListView):
    model = Student
    template_name = 'enroll/student.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'students'
    ordering = ['id']

 

class StudentDetailView(LoginRequiredMixin,DetailView):
    model = Student

  

class StudentCreateView(LoginRequiredMixin,  CreateView):
    model = Student
    fields = ['name','email','school','state','country','grade']

    def form_valid(self, form):
        form.instance.parent= self.request.user
        return super().form_valid(form)



class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Student
    fields = ['name','email','school','state','country','grade']

    def form_valid(self, form):
        form.instance.parent = self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user == student.parent:
            return True
        return False



