from django.shortcuts import render
#from django.contrib.auth.decorators import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Student
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = 'enroll/student.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'students'
    #ordering = ['-date_posted']


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Student
    fields = ['name','parent','email','school','state','country','grade']

    def form_valid(self, form):
        form.instance.parent= self.request.user
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Student
    fields = ['name','parent','email','school','state','country','grade']

    def form_valid(self, form):
        form.instance.parent = self.request.user
        return super().form_valid(form)

    def test_func(self):
        student = self.get_object()
        if self.request.user == student.parent:
            return True
        return False


class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Student
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == student.parent:
            return True
        return False

