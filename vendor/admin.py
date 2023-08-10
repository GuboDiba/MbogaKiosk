from django.contrib import admin

# Register your models here.
from.models import Vendor

class VenderAdmin(admin.ModelAdmin):
    vendor = ("name","number","email","username","store_name","password","location")
    admin.site.register(Vendor)
    