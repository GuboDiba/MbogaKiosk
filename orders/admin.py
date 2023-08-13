from django.contrib import admin

# Register your models here.
from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ("product_name", "customer", "product", "payment", "quantity", "total_price")
admin.site.register(Order,OrderAdmin)