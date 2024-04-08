from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login' ),
    path('signup/', views.signupUser, name='signup' ),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('history/', views.history, name='history'),
    path('transport/', views.transport, name='transport'),
    path('touristPlaces/', views.places, name='touristPlaces'),
    path('restreviews/', views.restreviews, name='restreviews'), 
]