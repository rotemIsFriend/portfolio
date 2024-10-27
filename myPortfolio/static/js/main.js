const darkModeToggle = document.getElementById('dark-mode-toggle');
const isDarkMode = localStorage.getItem('dark-mode') === 'true';

// Update dark mode icon
function updateDarkModeIcon() {
    darkModeToggle.classList.toggle('fa-moon', !document.body.classList.contains('dark-mode'));
    darkModeToggle.classList.toggle('fa-sun', document.body.classList.contains('dark-mode'));
}

// Dark mode handling
if (isDarkMode) {
    document.body.classList.add('dark-mode');
    updateDarkModeIcon();
}

darkModeToggle.addEventListener('click', function () {
    document.body.classList.toggle('dark-mode');
    const darkModeEnabled = document.body.classList.contains('dark-mode');
    localStorage.setItem('dark-mode', darkModeEnabled);
    updateDarkModeIcon();
});

document.getElementById('contactForm').addEventListener('submit', function (event) {
  event.preventDefault();

  const formData = new FormData(this);
  const submitUrl = this.getAttribute('data-url');

  fetch(submitUrl, {
      method: 'POST',
      body: formData,
      headers: {
          'X-Requested-With': 'XMLHttpRequest',
      }
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
          Swal.fire({
              title: 'Success!',
              text: 'Message sent successfully!',
              icon: 'success',
              confirmButtonText: 'OK'
          });
          this.reset(); // Reset the form
      } else {
          Swal.fire({
              title: 'Error!',
              text: 'Please check your input and try again.',
              icon: 'error',
              confirmButtonText: 'OK'
          });
          console.error(data.errors); // Log form errors in the console
      }
  })
  .catch(error => {
      Swal.fire({
          title: 'Error!',
          text: 'Something went wrong. Please try again later.',
          icon: 'error',
          confirmButtonText: 'OK'
      });
      console.error('Error:', error);
  });
});
