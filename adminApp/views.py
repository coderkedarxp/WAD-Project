from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from TourApp.models import Restaurant, RestaurantImage, Category, TouristPlace, TouristPlaceImage, TouristPlaceReview, Accommodation, AccommodationImage, AccommodationReview
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

def is_admin(user):
    return user.is_authenticated and user.is_staff

def admin_login_required(view_func):
    actual_decorator = user_passes_test(
        lambda user: is_admin(user),
        login_url=reverse_lazy('loginAdmin'),
        redirect_field_name=None
    )

    def _wrapped_view(request, *args, **kwargs):
        if not actual_decorator(request.user):
            return HttpResponseRedirect(reverse_lazy('loginAdmin'))
        return view_func(request, *args, **kwargs)

    return _wrapped_view

@admin_login_required
def addRestaurant(request):
    if not request.user.is_staff:
        return redirect('/loginAdmin')
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        location=request.POST['location']
        description=request.POST['description']
        images=request.FILES.getlist('images')
        priceRange=request.POST.get('priceRange')
        categories=request.POST.getlist('categories')

        if Restaurant.objects.filter(mapLocation=location).exists():
            messages.error(request, 'Restaurant Already in the database')
            return redirect(reverse('addRestaurant'))
        
        restaurant=Restaurant.objects.create(
            name=name,
            address=address,
            mapLocation=location,
            description=description,
            priceRange=priceRange,
        )

        restaurant.save()

        for image in images:
            RestaurantImage.objects.create(
                restaurant=restaurant,
                image=image
            )
        
        for category in categories:
            cat=Category.objects.get(name=category)
            restaurant.categories.add(cat)

        messages.success(request, f'Restaurant added successfully with id {restaurant.id}')
        return redirect(reverse('addRestaurant'))
    
    return render(request, 'addRestaurant.html')

@admin_login_required
def addTouristPlace(request):
    if not request.user.is_staff:
        return redirect(reverse('loginAdmin'))
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        location=request.POST['location']
        description=request.POST['description']
        images=request.FILES.getlist('images')
        entryFees=request.POST.get('entryFees')
        categories=request.POST.getlist('categories')

        if TouristPlace.objects.filter(mapLocation=location).exists():
            messages.error(request, 'Place Already in the database')
            return redirect(reverse('addTouristPlace'))
        
        place=TouristPlace.objects.create(
            name=name,
            address=address,
            mapLocation=location,
            description=description,
            entryFees=entryFees,
        )

        place.save()

        for image in images:
            TouristPlaceImage.objects.create(
                place=place,
                image=image
            )
        
        for category in categories:
            cat=Category.objects.get(name=category)
            place.categories.add(cat)

        messages.success(request, f'Tourist Place added successfully with id {place.id}')
        return redirect(reverse('addTouristPlace'))
    
    return render(request, 'addTouristPlace.html')


@admin_login_required
def addAccommodation(request):
    if not request.user.is_staff:
        return redirect(reverse('loginAdmin'))
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        location=request.POST['location']
        description=request.POST['description']
        images=request.FILES.getlist('images')
        priceRange=request.POST.get('priceRange')
        categories=request.POST.getlist('categories')

        if Accommodation.objects.filter(mapLocation=location).exists():
            messages.error(request, 'Accommodation Already in the database')
            return redirect(reverse('addAccommodation'))
        
        accommodation=Accommodation.objects.create(
            name=name,
            address=address,
            mapLocation=location,
            description=description,
            priceRange=priceRange,
        )

        accommodation.save()

        for image in images:
            AccommodationImage.objects.create(
                accommodation=accommodation,
                image=image
            )
        
        for category in categories:
            cat=Category.objects.get(name=category)
            accommodation.categories.add(cat)

        messages.success(request, f'accommodation added successfully with id {accommodation.id}')
        return redirect(reverse('addAccommodation'))
    
    return render(request, 'addAccommodation.html')

def loginAdmin(request):
    if request.user.is_authenticated and not request.user.is_staff:
        logout(request)
        messages.success(request, 'Please login as admin')
        return redirect(reverse('loginAdmin'))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect(reverse('admin_dashboard'))  # Redirect to admin dashboard upon successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'admin_login.html')




@admin_login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect(reverse('loginAdmin'))
    return render(request, 'admin_dashboard.html')