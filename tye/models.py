from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from enroll.models import Student, OrderCourse, Order

class Course(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.ForeignKey('Instructor',default=1, on_delete=models.CASCADE)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    prerequisite = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    description = models.TextField()
    session = models.ForeignKey('Session', default=1, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    slug = models.SlugField()
    image = models.ImageField(default='default.jpg',upload_to='course_pics')
   
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tye-class', kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse ('enroll: add-to-cart', kwargs={
            'slug': self.slug
        })

    

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    leader = models.BooleanField(null=False)
    title =  models.CharField(max_length=50, default="")
    school = models.CharField(max_length=50)
    age = models.IntegerField()   
    bio = models.TextField()
    image = models.ImageField(default='default.jpg',upload_to='instructor_pics')
    active_status = models.BooleanField(default=False)

   
    def __str__(self):
        return self.name
    
   

class Session(models.Model):
    sessionName = models.CharField(max_length=50)
    active_status = models.BooleanField(default=False)

    def __str__(self):
        return self.sessionName

class Event(models.Model):
    title = models.CharField(max_length=100)
    speaker = models.CharField(max_length=100,default=False)
    date = models.DateTimeField(default=timezone.now)
    location = models.TextField()
    description = models.TextField()
    image = models.ImageField(default='default.jpg',upload_to='event_pics')

    def __str__(self):
        return self.title


