from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import StudentCreateForm
from .models import Student

# Create your views here.
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
