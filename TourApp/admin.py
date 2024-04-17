from django.contrib import admin
from .models import Restaurant, RestaurantImage, RestaurantReview
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(RestaurantImage)
admin.site.register(RestaurantReview)
