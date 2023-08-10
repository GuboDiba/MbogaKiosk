from django.contrib import admin



# Register your models here.
from.models import Notification
class NotificationAdmin(admin.ModelAdmin):
    notifications = ("message","date","recipient","type_of_notification")
    
    admin.site.register(Notification)