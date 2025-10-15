// Get HTML elements
const loading = document.getElementById('loading');
const error = document.getElementById('error');
const profile = document.getElementById('profile');
const nameField = document.getElementById('name');
const emailField = document.getElementById('email');

// Fetch user data
fetch('https://jsonplaceholder.typicode.com/users/1')
  .then(response => {
    if (!response.ok) {
      throw new Error('Failed to fetch user data');
    }
    return response.json();
  })
  .then(user => {
    // Hide loading message
    loading.style.display = 'none';

    // Display user info
    nameField.textContent = user.name;
    emailField.textContent = user.email;
    profile.style.display = 'block';
  })
  .catch(err => {
    // Hide loading and show error
    loading.style.display = 'none';
    error.textContent = `Error: ${err.message}`;
  });
