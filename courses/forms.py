# courses/forms.py
# courses/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Lesson, Module, Course, Quiz, Question

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_student']

class LessonCreationForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'video', 'pdf']

class ModuleCreationForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title', 'lessons']
        widgets = {
            'lessons': forms.CheckboxSelectMultiple
        }

class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'modules']
        widgets = {
            'modules': forms.CheckboxSelectMultiple
        }

class QuizCreationForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title']

class QuestionCreationForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'answer']