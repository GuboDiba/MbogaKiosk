from django.db import models
from  orders.models import Order

# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Order)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    quantity = models.PositiveIntegerField()
    shipping_cost = models.DecimalField(decimal_places=2,max_digits=10)
    payments_option = models.CharField(max_length=32)

def __str__(self):
    return self.price
  