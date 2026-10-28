from django.db import models
from django.db.models import Sum

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    pubdate = models.DateTimeField()
    rating = models.SmallIntegerField(default=1)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

    @property
    def availability_percentage(self):
        total_quantity = Book.objects.aggregate(sum_qty=Sum('quantity'))['sum_qty']
        if total_quantity and total_quantity > 0:
            return round((self.quantity / total_quantity) * 100, 2)
        return 0