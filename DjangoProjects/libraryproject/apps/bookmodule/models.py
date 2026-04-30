from django.db import models
from django.utils import timezone


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    pubdate = models.DateTimeField()
    rating = models.SmallIntegerField(default=1)
    publisher = models.ForeignKey(Publisher, null=True, blank=True, on_delete=models.SET_NULL, related_name='books')
    authors = models.ManyToManyField(Author, related_name='books')
    
    # For Lab 7 compatibility (old fields)
    author = models.CharField(max_length=50, default='Unknown')
    edition = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.title
    
    @property
    def availability_percentage(self):
        """Calculate percentage of total books as transient field"""
        total = Book.objects.aggregate(models.Sum('quantity'))['quantity__sum'] or 0
        if total == 0:
            return 0
        return round((self.quantity / total) * 100, 2)


class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name
