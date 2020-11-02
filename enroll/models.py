from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from tye.models import Course


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(User, null = True , on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    school = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=50, default='USA')
    grade = models.CharField(max_length=2)  
  

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})



class OrderCourse(models.Model):
    
    course = models.ForeignKey("tye.Course", on_delete=models.CASCADE)
    
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.course.name} "

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    courses = models.ManyToManyField(OrderCourse)
    start_date = models.DateTimeField(auto_now_add = True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.name

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code




  