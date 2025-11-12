from .models import Student, Course
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['name', 'usn', 'email', 'phone', 'age', 'course']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        # fields = ['name', 'code', 'credits', 'duration']

