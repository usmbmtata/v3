const darkModeToggle = document.getElementById('darkModeToggle');
const body = document.body;

// Check if user has a preferred color scheme stored
if (localStorage.getItem('darkMode') === 'enabled') {
    enableDarkMode();
}

// Function to enable dark mode
function enableDarkMode() {
    body.classList.add('dark-mode');
    localStorage.setItem('darkMode', 'enabled');
}

// Function to disable dark mode
function disableDarkMode() {
    body.classList.remove('dark-mode');
    localStorage.setItem('darkMode', null);
}

// Toggle dark mode on button click
darkModeToggle.addEventListener('click', () => {
    if (body.classList.contains('dark-mode')) {
        disableDarkMode();
    } else {
        enableDarkMode();
    }
});
