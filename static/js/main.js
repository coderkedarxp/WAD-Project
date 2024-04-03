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