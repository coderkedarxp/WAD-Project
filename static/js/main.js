AOS.init();

const scrollRevealOption = {
    distance: "50px",
    origin: "bottom",
    duration: 1000.
};

//header container
ScrollReveal().reveal(".header__container h1", scrollRevealOption);

ScrollReveal().reveal(".header__container h4", {
    ...scrollRevealOption,
    delay: 500,
});

ScrollReveal().reveal(".header__container .btn", {
    ...scrollRevealOption,
    delay: 1000,
});

document.querySelector(".discover__btn").addEventListener("click", function() {
    window.location.href = "restaurants.html"; // Replace "new-page.html" with the URL of the page you want to redirect to
});

var a = 1; //show and unshow password
    function pass(){
        var passwordField = document.getElementById('password');
        var passIcon = document.getElementById('pass-icon');

        if(a == 1) {
            passwordField.type = "text";
            passIcon.classList.remove('fa-eye-slash');
            passIcon.classList.add('fa-eye');
            a = 0;
        } else {
            passwordField.type = "password";
            passIcon.classList.remove('fa-eye');
            passIcon.classList.add('fa-eye-slash');
            a = 1;
        }
    }

    var b = 1; //show and unshow password
    function confirmpass(){
        var passwordField = document.getElementById('confirmpassword');
        var passIcon = document.getElementById('confirmpass-icon');

        if(b == 1) {
            passwordField.type = "text";
            passIcon.classList.remove('fa-eye-slash');
            passIcon.classList.add('fa-eye');
            b = 0;
        } else {
            passwordField.type = "password";
            passIcon.classList.remove('fa-eye');
            passIcon.classList.add('fa-eye-slash');
            b = 1;
        }
    }

    var c = 0; // Initial state
function likeOrNone() {
    var likeIcon = document.getElementById('like-review');
    // Toggle the 'fa-solid' class based on the current state
    if (c === 0) {
        likeIcon.classList.add('fa-solid');
        c = 1;
    } else {
        likeIcon.classList.remove('fa-solid');
        likeIcon.classList.add('fa-regular')
        c = 0;
    }
}

var d = 0;
function unlikeOrNone() {
    var unlikeIcon = document.getElementById('unlike-review');
    if(d === 0) {
        unlikeIcon.classList.add('fa-solid');
        d = 1;
    } else {
        unlikeIcon.classList.remove('fa-solid');
        unlikeIcon.classList.add('fa-regular');
        d = 0;
    }
}


var myCarousel = document.getElementById('carouselExampleIndicators');
var carousel = new bootstrap.Carousel(myCarousel, {
    interval: 2000 // Adjust the interval as needed
});