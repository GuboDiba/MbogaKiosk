from django.contrib import admin

# Register your models here.
from.models import Cart

class CartAdmin(admin.ModelAdmin):
    cart = ("orders", "price","quantity","shipping","payment_option")
admin.site.register(Cart,CartAdmin)