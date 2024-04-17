from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CustomUser(AbstractUser):
    gender = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.username

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=100000)
    mapLocation = models.TextField(max_length=100000)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    description = models.TextField(max_length=1000000)
    categories = models.ManyToManyField(Category)
    priceRange=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, related_name='restaurant_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='restaurant_images/')

    def __str__(self):
        return f"Image for {self.restaurant.name}"


class RestaurantReview(models.Model):
    restaurant = models.ForeignKey( Restaurant, related_name='restaurant_review', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='restaurant_user',on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment=models.TextField(max_length=1000000)


@receiver(post_delete, sender=RestaurantImage)
def delete_restaurant_image(sender, instance, **kwargs):
    instance.image.delete(save=False)


class TouristPlace(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=100000)
    mapLocation = models.TextField(max_length=100000)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    description = models.TextField(max_length=1000000)
    categories = models.ManyToManyField(Category)
    entryFees=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class TouristPlaceImage(models.Model):
    place = models.ForeignKey(
        TouristPlace, related_name='tourist_place_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tourist_place_images/')

    def __str__(self):
        return f"Image for {self.place.name}"

class TouristPlaceReview(models.Model):
    place = models.ForeignKey( TouristPlace, related_name='tourist_place_review', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='place_user',on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment=models.TextField(max_length=1000000)

@receiver(post_delete, sender=TouristPlaceImage)
def delete_tourist_place_image(sender, instance, **kwargs):
    instance.image.delete(save=False)



class Accommodation(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=100000)
    mapLocation = models.TextField(max_length=100000)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    description = models.TextField(max_length=1000000)
    categories = models.ManyToManyField(Category)
    priceRange = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class AccommodationImage(models.Model):
    accommodation = models.ForeignKey(
        Accommodation, related_name='accommodation_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='accommodation_images/')

    def __str__(self):
        return f"Image for {self.accommodation.name}"

class AccommodationReview(models.Model):
    accommodation = models.ForeignKey(
        Accommodation, related_name='accommodation_reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='accommodation_user', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(max_length=1000000)

@receiver(post_delete, sender=AccommodationImage)
def delete_accommodation_image(sender, instance, **kwargs):
    instance.image.delete(save=False)


class UserPost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    caption = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='user_posts/')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    location = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Post by {self.user.username} at {self.location}"

@receiver(post_delete, sender=UserPost)
def delete_accommodation_image(sender, instance, **kwargs):
    instance.image.delete(save=False)