from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.title