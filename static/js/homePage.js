document.addEventListener('DOMContentLoaded', function() {
    // Get the toast element
    var toast = document.getElementById('toast-bottom-right');

    // Set a timeout to remove the toast after 2 seconds
    setTimeout(function() {
        if (toast) {
            toast.style.transition = 'opacity 0.5s ease';
            toast.style.opacity = '0';

            // Remove the toast from the DOM after the fade-out transition
            setTimeout(function() {
                if (toast) {
                    toast.remove();
                }
            }, 500); // Match this duration with the transition duration
        }
    }, 2000); // 2 seconds
});