from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=10)
    credits = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=40)
    usn = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    age = models.IntegerField()

    course = models.ForeignKey(Course, on_delete=models.CASCADE)