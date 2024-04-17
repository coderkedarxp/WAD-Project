from django.urls import path
from . import views

urlpatterns = [
    path('addRestaurant/', views.addRestaurant, name='addRestaurant'),
    path('addTouristPlace/', views.addTouristPlace, name='addTouristPlace'),
    path('addAccommodation/', views.addAccommodation, name='addAccommodation'),
    path('loginAdmin/', views.loginAdmin, name='loginAdmin'),
    path('', views.admin_dashboard, name='admin_dashboard'),
]