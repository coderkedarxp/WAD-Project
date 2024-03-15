let intro = document.querySelector('.intro');
let logo = document.querySelector('.logo');
let logoSpan = document.querySelectorAll('.logo-parts');
let animationCompleted = false;

window.addEventListener('DOMContentLoaded', () => {
    if (!animationCompleted) { // Check if the animation has not been completed yet
        setTimeout(() => {
            logoSpan.forEach((span, index) => {
                setTimeout(() => {
                    span.classList.add('active');
                }, (index+1)*100);
            });

            setTimeout(() => {
                logoSpan.forEach((span, index) => {
                    setTimeout(() => {
                        span.classList.remove('active');
                        span.classList.add('fade');
                    }, (index+1)*50);
                });
            }, 2000);

            setTimeout(() => {
                intro.style.top = '-100vh'; // Slide up the window
                animationCompleted = true; // Set the flag to true after the animation completes
            }, 2300);
            
        });
    }
});
