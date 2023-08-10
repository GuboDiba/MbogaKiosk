from django.db import models

# Create your models here.
class Notification(models.Model):
    message = models.TextField()
    date = models.DateField()
    recipient = models.CharField(max_length=32)
    type_of_notification = models.TextField()
    
    def __str__(self):
       return self.message

   