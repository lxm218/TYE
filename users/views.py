from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm, StudentCreateForm
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def student(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        s_form = StudentCreateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.student)
        if s_form.is_valid() and u_form.is_valid():
            u_form.save()
            s_form.save()
            messages.success(request, f'Your student has been added!')
            return redirect('student')

    else:
        u_form = UserUpdateForm(instance=request.user)
        s_form = StudentCreateForm(instance=request.user.student)

    context = {
        'u_form': u_form,
        's_form': s_form
    }
    return render(request, 'users/student.html',context)