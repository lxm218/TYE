from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    image = models.ImageField(default='default.jpg',upload_to='course_pics')


  
        
    def __str__(self):
        return self.name

    

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    leader = models.BooleanField(null=False)
    title =  models.CharField(max_length=50, default="")
    school = models.CharField(max_length=50)
    age = models.CharField(max_length=50)   
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

class Student(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, null = True , on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    school = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=50, default='USA')
    grade = models.CharField(max_length=2)   
  

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save()
