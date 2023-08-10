from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=32)
    products =models.PositiveIntegerField()
    locations = models.CharField(max_length=50)
    delivery = models.CharField(max_length=50)
def __str__(self):
    return self.name