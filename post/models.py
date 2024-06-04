from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return f'{self.id}. {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, models.CASCADE, related_name='products')

    def __str__(self):
        return f'{self.id}. {self.name}'


class Store(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.id}. {self.name}'