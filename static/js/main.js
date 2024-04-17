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

document.querySelector(".discover__btn").addEventListener("click", function () {
    window.location.href = "restaurants.html"; // Replace "new-page.html" with the URL of the page you want to redirect to
});

var a = 1; //show and unshow password
function pass() {
    var passwordField = document.getElementById('password');
    var passIcon = document.getElementById('pass-icon');

    if (a == 1) {
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
function confirmpass() {
    var passwordField = document.getElementById('confirmpassword');
    var passIcon = document.getElementById('confirmpass-icon');

    if (b == 1) {
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
    if (d === 0) {
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

function showMap1() {
    window.location.href = "https://maps.app.goo.gl/1Qv86AQUtBJJ1iRZ6";
}

function showMap2() {
    window.location.href = "https://www.google.com/search?sca_esv=421bbcb432c7b64f&sca_upv=1&rlz=1C1CHBF_enIN1050IN1050&tbs=lf:1,lf_ui:9&tbm=lcl&sxsrf=ACQVn09zcV2fdRZ8h-W2yhpGRys0_w3wtQ:1713091532825&q=famous+misal+places+in+pune&rflfq=1&num=10&sa=X&ved=2ahUKEwiul6Ciw8GFAxXPXmwGHWx7Cw8QjGp6BAheEAE&biw=1280&bih=631&dpr=1.5#rlfi=hd:;si:;mv:[[18.642255062227573,73.87499662291363],[18.483755552099826,73.57973905455425]]";
}

function showMap3() {
    window.location.href = "https://www.google.com/maps/search/famous+bhakarwadi+in+pune/@18.4678717,73.7757159,13z/data=!3m1!4b1?entry=ttu";
}

function viewmorecuisine() {
    window.location.href = "https://www.google.com/search?sca_esv=421bbcb432c7b64f&sca_upv=1&rlz=1C1CHBF_enIN1050IN1050&tbs=lf:1,lf_ui:9&tbm=lcl&sxsrf=ACQVn0-bdQSmUKRA0VjcKUd_elM2rwN5Mw:1713093166073&q=famous+street+food+in+pune&rflfq=1&num=10&sa=X&ved=2ahUKEwjA14WtycGFAxV8S2wGHXlqDWgQjGp6BAheEAE&biw=1280&bih=631&dpr=1.5#rlfi=hd:;si:;mv:[[18.6097124,73.922821],[18.4523465,73.8004725]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u5!2m2!5m1!1sgcid_3fast_1food_1restaurant!1m4!1u5!2m2!5m1!1sgcid_3north_1indian_1restaurant!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e5!2m1!1e3!3sIAEqAklO,lf:1,lf_ui:9";
}