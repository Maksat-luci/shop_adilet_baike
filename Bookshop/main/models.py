from django.db import models


CHOICES = (
    ('ins stock', ' в наличии'),
    ('out of stock', 'нет в наличии')
)
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.name} {self.last_name}'



class Genre(models.Model):
    slug = models.SlugField(primary_key=True, max_length=20)
    name = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return f'{self.name}'








class Book(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='books',blank=True,null=True)
    status = models.CharField(max_length=20,choices=CHOICES)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name= 'books')
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f'{self.title} - {self.author}'









