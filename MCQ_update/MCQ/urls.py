"""MCQ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mcq import views

urlpatterns = [
    path('',views.about,name='about'),
    path('admin/', admin.site.urls),
    path('accounts/signup/',views.SignUpView.as_view(),name='signup'),
    path('teacher/', views.TeacherTemplate.as_view(), name='quiz_change_list'),
    path('student/', views.StudentTemplate.as_view(), name='quiz_list'),
    path('accounts/signup/student/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', views.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
]
