from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')

class StudentSignUpForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user

class TeacherSignUpForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        return user
