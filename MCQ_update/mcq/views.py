from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
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
from .forms import StudentSignUpForm,TeacherSignUpForm,UserForm
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

class SignUpView(TemplateView):
    template_name = 'signup.html'

class StudentTemplate(TemplateView):
    template_name = 'student_index.html'

class TeacherTemplate(TemplateView):
    template_name = 'teacher_index.html'

class StudentSignUpView(CreateView):
    model = User
    template_name = 'registration/signup_form.html'
    user_form = StudentSignUpForm
    fields = ('username','password','email')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('quiz_list')

class TeacherSignUpView(CreateView):
    fields = ('username','password','email')
    model = User
    template_name = 'registration/signup_form.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('quiz_change_list')

def about(request):
    return render(request,'about.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('about')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        u = User.objects.filter(username=username,password=password)
        print(u.values())
        print(u.values('is_student','is_teacher'))
        print(u[0].is_student)

        user = authenticate(username=username,password=password)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                print("x")
                if u[0].is_student == False:
                    return HttpResponseRedirect(reverse('student_index'))
                else:
                    return HttpResponseRedirect(reverse('teacher_index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            return HttpResponse("invalid login details provided")
    else:
        form = UserForm()
        return render(request,'registration/login.html',{'form':form})
