from django.db import models

class Book(models.Model):
    bookName = models.CharField(max_length=50)
    authorName = models.CharField(max_length=50)
    publishedDate = models.CharField(max_length=10)
    ratings = models.IntegerField(default=0)
    price = models.FloatField()

    def __str__(self):
        return f'{self.bookName} — {self.authorName}'