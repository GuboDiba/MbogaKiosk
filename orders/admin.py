from django.contrib import admin

# Register your models here.
from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name','locations','delivery','products')
admin.site.register(Order,OrderAdmin)