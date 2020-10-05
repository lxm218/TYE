from django.shortcuts import render
from .models import Course, Instructor, Session, Event, Student
from django.contrib.auth.decorators import login_required
from .forms import StudentCreateForm


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
        'instructors': Instructor.objects.all()
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

@login_required
def student(request):
    if request.method == 'POST':
        s_form = StudentCreateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.student)
        if s_form.is_valid() and u_form.is_valid():
            u_form.save()
            s_form.save()
            messages.success(request, f'Your student has been added!')
            return redirect('student')

    else:
        s_form = StudentCreateForm(instance=request.user.student)

    context = {
        's_form': s_form
    }
    return render(request, 'student.html',context)






