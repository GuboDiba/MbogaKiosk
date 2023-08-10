from django.db import models

# Create your models here.
class Rating(models.Model):
    review_message = models.TextField()
    sender = models.CharField(max_length=32)
    star_rating = models.IntegerField()
    date = models.DateField()
    
def __str__(self):
    return Rating

