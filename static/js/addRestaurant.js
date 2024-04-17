document.addEventListener('DOMContentLoaded', function() {
    let non_veg = document.querySelector('#non_veg');
    let pure_veg = document.querySelector('#pure_veg');

    // Function to handle changes in the non-veg checkbox
    non_veg.addEventListener('change', function(event) {
        if (non_veg.checked && pure_veg.checked) {
            pure_veg.checked = false;
        }
        pure_veg.disabled = non_veg.checked;
    });

    // Function to handle changes in the pure veg checkbox
    pure_veg.addEventListener('change', function(event) {
        if (pure_veg.checked && non_veg.checked) {
            non_veg.checked = false;
        }
        non_veg.disabled = pure_veg.checked;
    });
});
