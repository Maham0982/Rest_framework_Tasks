from django.db import models

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField()
    date_of_birth=models.DateField()

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name=models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date=models.DateField()

    def __str__(self):
        return self.title
    



