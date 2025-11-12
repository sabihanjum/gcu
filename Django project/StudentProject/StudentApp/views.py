# ...existing code...
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import StudentForm, CourseForm

def home(request):
    return render(request, 'index.html')

def addstudent(request):
    errors = None
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            # Redirect to admin change list so you can see the record immediately
            return redirect(reverse('admin:StudentApp_student_changelist'))
        else:
            errors = form.errors  # pass form errors to template for debugging
    else:
        form = StudentForm()

    data = {'sform': form, 'form_errors': errors}
    return render(request, 'addstudent.html', data)

def addcourse(request):
    courseform = CourseForm()
    data = {
        'form': courseform,
    }
    return render(request, 'addcourse.html', data)
# ...existing code...