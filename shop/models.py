from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    description  = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')

    class Meta:
        db_table = 'products'
