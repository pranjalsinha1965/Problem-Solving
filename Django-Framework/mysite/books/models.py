from django.db import models

# Create your models here.
class Author(models.Model): 
    name = models.CharField(max_length=100)
    brithdate = models.DateField()

    def __str__(self): 
        return self.name

class Book(models.Model): 
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.CharField(
        max_length=2
    )
    isbn = models.CharField(max_length=13, unique=True)
    published = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self): 
        return self.title
    