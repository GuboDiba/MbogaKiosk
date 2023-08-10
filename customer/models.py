from django.db import models
from orders.models import Order

# Create your models here.
class Customer(models.Model):
    orders =models.ManyToManyField(Order)
    name = models.CharField(max_length=32)
    phone_number = models.IntegerField()
    email_address = models.EmailField()
    
    def __str__(self):
        return self.name
    