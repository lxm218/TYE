from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tye.models import Course

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





  