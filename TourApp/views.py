from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from .models import CustomUser, Restaurant, RestaurantImage, RestaurantReview, TouristPlaceImage, TouristPlace, TouristPlaceReview, Category, Accommodation, AccommodationImage, AccommodationReview, UserPost
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
import operator
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def home(request):
    posts=list(UserPost.objects.all())
    count=len(posts)
    if count>6:
        posts=posts[0:6]
    
    for post in posts:
        temp = str(post.content_type.model_class())
        if (operator.contains(temp, 'TouristPlace')):
            post.link = 'touristPlace'
        elif (operator.contains(temp, 'Restaurant')):
            post.link = 'restaurant'
        else:
            post.link = 'accommodation'
    context={
        'posts':posts,
    }
    return render(request, 'index.html', context)


def logoutUser(request):
    logout(request)
    messages.success(request, 'Logged Out Sucessfully!')
    return redirect('/')


def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']

            if not CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Invalid Username')
                return redirect('/login/')

            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request, 'Wrong Password')
                return redirect('/login/')

            else:
                login(request, user)
                return redirect('/')

        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return redirect('/login/')

    return render(request, 'login.html', context={'title':'Login'})


def signupUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username'].lower()
            gender = form.cleaned_data['gender']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirmpassword = form.cleaned_data['confirmpassword']

            if (password != confirmpassword):
                messages.error(
                    request, 'Passwords did not match. Please try again')
                return redirect('/signup/')

            user = CustomUser.objects.filter(username=username)

            if user.exists():
                messages.error(request, 'Username Already Taken')
                return redirect('/signup/')
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Taken')
                return redirect('/signup/')
            else:
                user = CustomUser.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    gender=gender,
                    email=email,
                    username=username)

                user.set_password(password)
                user.save()
                messages.success(request, 'Account Created Successfully!')

                return render(request, 'login.html', {'title': 'Login'})
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return redirect('/signup/')
    return render(request, 'signup.html', context={'title':'Sign Up'})


@login_required(login_url='/login/')
def restaurants(request):
    categories = request.GET.getlist('category')

    # Retrieve all places
    all_restaurants = Restaurant.objects.all()

    # Apply filters based on selected categories
    if categories:
        all_restaurants = all_restaurants.filter(
            categories__name__in=categories).distinct()

    # Prepare data for rendering
    restaurants = []
    for restaurant in all_restaurants:
        # Calculate rating
        reviews = RestaurantReview.objects.filter(restaurant=restaurant)
        total_reviews = len(reviews)
        total_rating = sum(review.rating for review in reviews)
        rating = round(total_rating / total_reviews, 1) if total_reviews else 0

        # Retrieve image
        image = RestaurantImage.objects.filter(restaurant=restaurant).first()

        # Append data to places list
        restaurants.append(
            {'restaurant': restaurant, 'image': image, 'rating': rating})

    # Pass filtered places and checked categories to the template
    context = {
        'restaurants': restaurants,
        'checked': categories,
        'title':'Restaurants In Pune',
    }

    return render(request, 'restaurants.html', context)


@login_required(login_url='/login/')
def restreviews(request, id):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        user = request.user
        restaurant = Restaurant.objects.get(id=id)
        rating = int(rating)

        review = RestaurantReview.objects.create(
            restaurant=restaurant,
            user=user,
            rating=rating,
            comment=comment
        )

        review.save()

        messages.success(request, 'Review added successfully!')
        messages.success(request, 'We appreciete contribution ♥️!')

        return redirect(f'/restaurant/{id}')

    restaurant = Restaurant.objects.get(id=id)
    if restaurant is None:
        messages.error('Restaurant Does not exist!')
        redirect('/restaurants/')

    images = list(RestaurantImage.objects.filter(restaurant=restaurant))
    reviews = list(RestaurantReview.objects.filter(restaurant=restaurant))
    categories = list(restaurant.categories.all())
    isLess = True

    if len(reviews) > 10:
        reviews = reviews[:10]
        isLess = False

    for review in reviews:
        review.stars = range(review.rating)

    context = {
        'restaurant': restaurant,
        'images': images,
        'reviews': reviews,
        'isLess': isLess,
        'categories': categories,
        'title': restaurant.name,
    }
    return render(request, 'restreviews.html', context)


@login_required(login_url='/login/')
def history(request):
    return render(request, 'history.html', context={'title':'History'})

@login_required(login_url='/login/')
def food(request):
    return render(request, 'food.html', context={'title':'Food'})


@login_required(login_url='/login/')
def transport(request):
    return render(request, 'transport.html', context={'title':'Transport'})


@login_required(login_url='/login/')
def places(request):
    # Retrieve selected categories from query parameters
    categories = request.GET.getlist('category')

    # Retrieve all places
    all_places = TouristPlace.objects.all()

    # Apply filters based on selected categories
    if categories:
        all_places = all_places.filter(
            categories__name__in=categories).distinct()

    # Prepare data for rendering
    places = []
    for place in all_places:
        # Calculate rating
        reviews = TouristPlaceReview.objects.filter(place=place)
        total_reviews = len(reviews)
        total_rating = sum(review.rating for review in reviews)
        rating = round(total_rating / total_reviews, 1) if total_reviews else 0

        # Retrieve image
        image = TouristPlaceImage.objects.filter(place=place).first()

        # Append data to places list
        places.append({'place': place, 'image': image, 'rating': rating})

    # Pass filtered places and checked categories to the template
    context = {
        'places': places,
        'checked': categories,
        'title':'Places To Visit',
    }

    return render(request, 'places.html', context)


@login_required(login_url='/login/')
def allReviews(request, query):
    model, id = query.split('+')

    if model.lower() == 'restaurant':
        restaurant = Restaurant.objects.get(id=id)
        reviews = list(RestaurantReview.objects.filter(restaurant=restaurant))
        for review in reviews:
            review.stars = range(review.rating)

        context = {
            'restaurant': restaurant,
            'reviews': reviews,
            'title': f'Reviews - {restaurant.name}'
        }

    elif model.lower() == 'touristplace':
        place = TouristPlace.objects.get(id=id)
        reviews = list(TouristPlaceReview.objects.filter(place=place))
        for review in reviews:
            review.stars = range(review.rating)

        context = {
            'place': place,
            'reviews': reviews,
            'title': f'Reviews - {place.name}'
        }
    else:
        lodge = Accommodation.objects.get(id=id)
        reviews = list(AccommodationReview.objects.filter(accommodation=lodge))
        for review in reviews:
            review.stars = range(review.rating)

        context = {
            'lodge': lodge,
            'reviews': reviews,
            'title': f'Reviews - {lodge.name}'
        }

    return render(request, 'allReviews.html', context)


@login_required(login_url='/login/')
def touristPlace(request, id):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        user = request.user
        place = TouristPlace.objects.get(id=id)
        rating = int(rating)

        review = TouristPlaceReview.objects.create(
            place=place,
            user=user,
            rating=rating,
            comment=comment
        )

        review.save()

        messages.success(request, 'Review added successfully!')
        messages.success(request, 'We appreciete contribution ♥️!')

        return redirect(f'/touristPlace/{id}')

    place = TouristPlace.objects.get(id=id)
    if place is None:
        messages.error('Place does not exist')
        redirect('/touristPlaces/')

    images = list(TouristPlaceImage.objects.filter(place=place))
    reviews = list(TouristPlaceReview.objects.filter(place=place))
    categories = list(place.categories.all())
    isLess = True

    if len(reviews) > 10:
        reviews = reviews[:10]
        isLess = False

    for review in reviews:
        review.stars = range(review.rating)

    context = {
        'place': place,
        'images': images,
        'reviews': reviews,
        'isLess': isLess,
        'categories': categories,
        'title': place.name,
    }
    return render(request, 'touristPlace.html', context)


@login_required(login_url='/login/')
def lodges(request):
    categories = request.GET.getlist('category')

    # Retrieve all places
    all_lodges = Accommodation.objects.all()

    # Apply filters based on selected categories
    if categories:
        all_lodges = all_lodges.filter(
            categories__name__in=categories).distinct()

    # Prepare data for rendering
    lodges = []
    for lodge in all_lodges:
        # Calculate rating
        reviews = AccommodationReview.objects.filter(accommodation=lodge)
        total_reviews = len(reviews)
        total_rating = sum(review.rating for review in reviews)
        rating = round(total_rating / total_reviews, 1) if total_reviews else 0

        # Retrieve image
        image = AccommodationImage.objects.filter(accommodation=lodge).first()

        # Append data to places list
        lodges.append({'lodge': lodge, 'image': image, 'rating': rating})

    # Pass filtered places and checked categories to the template
    context = {
        'lodges': lodges,
        'checked': categories,
        'title': 'Accommodation',
    }

    return render(request, 'accommodations.html', context)


@login_required(login_url='/login/')
def nature(request):
    return render(request, 'nature.html', context={'title':'Nature'})


@login_required(login_url='/login/')
def culture(request):
    return render(request, 'culture.html', context={'title':'Culture'})


@login_required(login_url='/login')
def gallery(request):
    usersPosts = UserPost.objects.filter(user=request.user)
    otherPosts = UserPost.objects.filter(~Q(user=request.user))

    for post in usersPosts:
        temp = str(post.content_type.model_class())
        if (operator.contains(temp, 'TouristPlace')):
            post.link = 'touristPlace'
        elif (operator.contains(temp, 'Restaurant')):
            post.link = 'restaurant'
        else:
            post.link = 'accommodation'

    for post in otherPosts:
        temp = str(post.content_type.model_class())
        if (operator.contains(temp, 'TouristPlace')):
            post.link = 'touristPlace'
        elif (operator.contains(temp, 'Restaurant')):
            post.link = 'restaurant'
        else:
            post.link = 'accommodation'

    context = {
        'usersPosts': usersPosts,
        'otherPosts': otherPosts,
        'title':' Gallery',
    }

    return render(request, 'gallery.html', context)


@login_required(login_url='/login')
def addPost(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        caption = request.POST.get('caption')
        location = request.POST.get('location')
        location_type, id, name = location.split('_')
        user = request.user

        if location_type == 'restaurant':
            loc = Restaurant.objects.get(id=id)
            restaurant_post = UserPost.objects.create(
                user=user,
                caption=caption,
                image=image,
                content_type=ContentType.objects.get_for_model(Restaurant),
                object_id=loc.id,
                location=loc
            )
            restaurant_post.save()
            messages.success(request, 'Your post is added successfully!')
            return redirect('/gallery')

        elif location_type == 'place':
            loc = TouristPlace.objects.get(id=id)
            place_post = UserPost.objects.create(
                user=user,
                caption=caption,
                image=image,
                content_type=ContentType.objects.get_for_model(TouristPlace),
                object_id=loc.id,
                location=loc
            )
            place_post.save()
            messages.success(request, 'Your post is added successfully!')
            return redirect('/gallery')
        else:
            loc = Accommodation.objects.get(id=id)
            acc_post = UserPost.objects.create(
                user=user,
                caption=caption,
                image=image,
                content_type=ContentType.objects.get_for_model(Accommodation),
                object_id=loc.id,
                location=loc
            )
            acc_post.save()
            messages.success(request, 'Your post is added successfully!')
            return redirect('/gallery')

    restaurants = list(Restaurant.objects.all())
    places = list(TouristPlace.objects.all())
    lodges = list(Accommodation.objects.all())

    context = {
        'restaurants': restaurants,
        'places': places,
        'lodges': lodges,
        'title':'Add Post',
    }

    return render(request, 'addPost.html', context=context)


def delete_review(request, query):
    loc, id = query.split('+')
    if loc == 'Restaurant':
        review = RestaurantReview.objects.get(id=id)
        loc_id = review.restaurant.id
    elif loc == 'touristPlace':
        review = TouristPlaceReview.objects.get(id=id)
        loc_id = review.place.id
    else:
        review = AccommodationReview.objects.get(id=id)
        loc_id = review.accommodation.id

    review.delete()
    messages.success(request, "Your review has been deleted")
    return redirect(f'/{loc}/{loc_id}')


@login_required(login_url='/login')
def userProfile(request):
    posts = list(UserPost.objects.filter(user=request.user))
    count = len(posts)
    for post in posts:
        temp = str(post.content_type.model_class())
        if (operator.contains(temp, 'TouristPlace')):
            post.link = 'touristPlace'
        elif (operator.contains(temp, 'Restaurant')):
            post.link = 'restaurant'
        else:
            post.link = 'accommodation'
    context = {
        'posts': posts,
        'count': count,
        'title':f'User Profile - {request.user.username}'
    }

    return render(request, 'userProfile.html', context)


@login_required(login_url='/login')
def deletePost(request, id):
    post = UserPost.objects.get(id=id)

    post.delete()

    messages.success(request, 'Post has been deleted successfully!')
    return redirect('/userProfile')


@login_required(login_url='/login')
def editProfile(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')

        current_user = request.user

        if username != current_user.username:
            if CustomUser.objects.filter(username=username).exists():
                messages.success(request, 'Username already taken')
                return redirect('/editProfile')
            elif CustomUser.objects.filter(email=email).exists():
                messages.success(request, 'Email already taken')
                return redirect('/editProfile')
            else:
                current_user.username = username
                current_user.first_name = first_name
                current_user.last_name = last_name
                current_user.email = email
                current_user.gender = gender
                current_user.save()
                messages.success(request, 'Profile updates successfully')

            
        else:
            if current_user.email != email and  CustomUser.objects.filter(email=email).exists():
                messages.success(request, 'Email already taken')
                return redirect('/editProfile')
            current_user.username = username
            current_user.first_name = first_name
            current_user.last_name = last_name
            current_user.email = email
            current_user.gender = gender
            current_user.save()
            messages.success(request, 'Profile updates successfully')

        return redirect('/userProfile')
    return render(request, 'editProfile.html', context={'title':f'Edit Profile - {request.user.username}'})

def changePassword(request):
    if request.method == 'POST':
        old_password = request.POST.get('oldPassword')
        new_password = request.POST.get('newPassword')
        confirm_new_password = request.POST.get('ConfirmNewPassword')

        if new_password != confirm_new_password:
            messages.error(request, "New password and confirm password do not match.")
            return redirect('/changePassword')

        user = request.user

        if not user.check_password(old_password):
            messages.error(request, "Your old password was entered incorrectly. Please enter it again.")
            return redirect('/changePassword')

        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user) 
        messages.success(request, 'Your password was successfully updated!')
        return redirect('/editProfile')
    return render(request, 'changePassword.html', content_type={'title':f'Change Password - {request.user.username}'})


def accommodation(request, id):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        user = request.user
        lodge = Accommodation.objects.get(id=id)
        rating = int(rating)

        review = AccommodationReview.objects.create(
            accommodation=lodge,
            user=user,
            rating=rating,
            comment=comment
        )

        review.save()

        messages.success(request, 'Review added successfully!')
        messages.success(request, 'We appreciete contribution ♥️!')

        return redirect(f'/accommodation/{id}')

    lodge = Accommodation.objects.get(id=id)
    if lodge is None:
        messages.error('Does not exist')
        redirect('/accommodations/')

    images = list(AccommodationImage.objects.filter(accommodation=lodge))
    reviews = list(AccommodationReview.objects.filter(accommodation=lodge))
    categories = list(lodge.categories.all())
    isLess = True

    if len(reviews) > 10:
        reviews = reviews[:10]
        isLess = False

    for review in reviews:
        review.stars = range(review.rating)

    context = {
        'lodge': lodge,
        'images': images,
        'reviews': reviews,
        'isLess': isLess,
        'categories': categories,
        'title':lodge.name,
    }
    return render(request, 'accommodation.html', context)

@login_required(login_url='/login')
def deleteAccount(request):
    user=request.user
    user.delete()
    logout(request)
    messages.success(request, 'Your account has been deleted successfully!')
    return redirect('/login')