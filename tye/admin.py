from django.contrib import admin
from .models import Course, Instructor,Session

# Register your models here.

from django.contrib import admin
from .models import Course, Instructor,Session,Event

# Register your models here.
admin.site.register(Course)

admin.site.register(Instructor)

admin.site.register(Session)

admin.site.register(Event)



