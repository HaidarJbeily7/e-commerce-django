from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    description  = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')

    class Meta:
        db_table = 'products'


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email =models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)