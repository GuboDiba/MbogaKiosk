from django.contrib import admin

# Register your models here.
from.models import Customer
class CustomerAdmin(admin.ModelAdmin):
    customer = ("name","phone_number","email_address")
    
admin.site.register(Customer,CustomerAdmin)    
