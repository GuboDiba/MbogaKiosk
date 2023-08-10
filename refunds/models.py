from django.db import models

# Create your models here.
class Refunds(models.Model):
    amount = models.DecimalField(decimal_places=2,max_digits=6)
    payment_method = models.CharField(max_length=32)
    payment_method = models.DateField()
    receipt = models.CharField(max_length=32)
    status = models.CharField(max_length=32)
    orders = models.CharField(max_length=32)
    
def __str__(self):
    return self.amount
