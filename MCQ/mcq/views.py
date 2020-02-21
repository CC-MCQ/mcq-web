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

def student(user):
    return user.username.endswith("y")

def about(request):
    return render(request,'about.html')

@user_passes_test(student,login_url='/')
def index(request):
    return render(request,'index.html')
