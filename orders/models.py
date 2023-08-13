

from django.db import models
from payment.models import Payment
from inventory.models import Product
from customer.models import Customer
from customer.models import Customer

class Order(models.Model):
    # onetoone relationship between order and payment i.e each order instance is associated with 
    # one payment instance.
    
    # one to many relationship between order and product i.e  each Order instance can be associated with
    # one Product instance, but a Product instance can be related to multiple Order instances.

    product_name = models.CharField(max_length=32)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    

    #  order has one-to-many relationship with the Customer model using the ForeignKey field 
    # type. i.e each Order instance is associated with one Customer instance, but a Customer 
    # instance can have multiple related Order instances.
    # order has many-to-many relationship with the ShoppingCart model 
    # i.e multiple Order instances can be associated with multiple ShoppingCart instances, and vice versa.


    def __str__(self):
        return f"Order {self.pk}"












