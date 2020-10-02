from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'  
   
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)    

class Student(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(User, default = "" , on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    school = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=50, default='USA')
    grade = models.CharField(max_length=2)   
  

    def __str__(self):
        return self.name


   




