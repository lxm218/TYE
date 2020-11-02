from django.shortcuts import render, redirect
#from django.contrib.auth.decorators import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Student, OrderCourse, Order
from tye.models import Course
from django.utils import timezone
from django.contrib import messages
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



def add_to_cart(request,slug):
    course = get_object_or_404(Course, slug=slug)
    order_course = OrderCourse.objects.create(course = course)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.courses.filter(course_slug=course.slug).exists():
            order_course.quantity += 1
            order_course.save()
        else:
            order.courses.add(order_course)
            messages.info(request,"this course was added to your cart")
            return redirect('order-summary')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user = request.user, ordered_date=ordered_date)
        order.courses.add(order_course)

    return redirect('tye:tye-class', slug = slug)
