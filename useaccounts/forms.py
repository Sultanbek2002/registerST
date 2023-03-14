from django import forms
from .models import Student
from django.contrib.auth.admin import User


class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {'password': forms.PasswordInput()}
