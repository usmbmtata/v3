document.addEventListener('DOMContentLoaded', function () {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;

    // Function to toggle dark mode
    function toggleDarkMode() {
        body.classList.toggle('dark-mode', darkModeToggle.checked);

        // Save dark mode preference in local storage
        localStorage.setItem('darkMode', darkModeToggle.checked);
    }

    // Check local storage for dark mode preference on page load
    const savedDarkMode = localStorage.getItem('darkMode');
    if (savedDarkMode === 'true') {
        darkModeToggle.checked = true;
        toggleDarkMode();
    }

    // Event listener for the dark mode toggle
    darkModeToggle.addEventListener('change', toggleDarkMode);
});
