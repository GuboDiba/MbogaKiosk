from django.contrib import admin

# Register your models here.
from.models import Payment
class PaymentAdmin(admin.ModelAdmin):
    payments = ("amount","payment_method","payment_method","transaction_id","status")
    admin.site.register(Payment)
