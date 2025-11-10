from django.db import models



# Create your models here.
class Groom(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)