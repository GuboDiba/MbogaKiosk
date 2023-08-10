from django.contrib import admin

# Register your models here.
from.models import Rating

class RatingAdmin(admin.ModelAdmin):
    rating = ("review_message"," sender","star_rating","date")
admin.site.register(Rating)