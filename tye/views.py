from django.shortcuts import render
from .models import Course, Instructor, Session, Event
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):  
    return render(request, 'tye/home.html')

def about(request):  
    return render(request, 'tye/about.html')

def team(request):  
    return render(request, 'tye/team.html')

def leader(request):
    context = {
        'instructors': Instructor.objects.all()
    }
    return render(request, 'tye/leader.html',context)


def instructor(request):
    context = {
        # doc, https://docs.djangoproject.com/en/3.1/topics/db/queries/#lookups-that-span-relationships
        'instructors': Instructor.objects.filter(course__instructor__isnull=False)
    }
    return render(request, 'tye/instructor.html',context)

def course(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'tye/class.html',context)

def event(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'tye/event.html',context)




