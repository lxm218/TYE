from django.contrib import admin
from .models import Student, OrderCourse, Order

# Register your models here.
admin.site.register(Student)
admin.site.register(OrderCourse)
admin.site.register(Order)