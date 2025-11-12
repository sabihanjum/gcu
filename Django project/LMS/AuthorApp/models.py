from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorName = models.CharField(max_length=100)
    AuthorAge = models.IntegerField()
    AuthorPhone = models.CharField(max_length=20, blank=True)
    AuthorEmail = models.EmailField(unique=True)

    def __str__(self):
        return self.AuthorName