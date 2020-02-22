from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import  CreateView, UpdateView, DeleteView, FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django import forms
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .forms import UserForm,UserProfileInfoSite
from .models import UserProfileInfo
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def student(user):
    v = UserProfileInfo.objects.filter(user=user)
    print(v[0].identity)
    return (v[0].identity == 'student')

def teacher(user):
    v = UserProfileInfo.objects.filter(user=user)
    print(v[0].identity)
    return (v[0].identity == 'teacher')

def about(request):
    return render(request,'about.html')

@user_passes_test(student,login_url='/teacher_index')
def student_index(request):
    return render(request,'student_index.html')

@user_passes_test(teacher,login_url='/')
def teacher_index(request):
    return render(request,'teacher_index.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request,'about.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoSite(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoSite()

    return render(request,'registration.html',
                                    {'user_form':user_form,
                                     'profile_form':profile_form,
                                     'registered':registered})
