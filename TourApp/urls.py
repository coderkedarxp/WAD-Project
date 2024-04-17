from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login' ),
    path('signup/', views.signupUser, name='signup' ),
    path('logout/', views.logoutUser, name='logout' ),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('history/', views.history, name='history'),
    path('transport/', views.transport, name='transport'),
    path('touristPlaces/', views.places, name='touristPlaces'),
    path('nature/', views.nature, name='nature'),
    path('gallery/', views.gallery, name='gallery'),
    path('restaurant/<int:id>', views.restreviews, name='restaurant'), 
    path('touristPlace/<int:id>', views.touristPlace, name='touristPlace'), 
    path('allReviews/<str:query>', views.allReviews, name='allReviews'),
    path('addPost/', views.addPost, name='addPost'),
    path('culture/', views.culture, name='culture'),
    path('delete_review/<str:query>', views.delete_review, name='delete_review'),
    path('userProfile/', views.userProfile, name='userProfile'),
    path('deletePost/<int:id>', views.deletePost, name='deletePost'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('accommodations/', views.lodges, name='accommodations'),
    path('accommodation/<int:id>', views.accommodation, name='accommodation'),
    path('food/', views.food, name='food'),
    path('deleteAccount/', views.deleteAccount, name='deleteAccount'),

]