// ============================================
// Authentication and Cookie Management
// ============================================

const API_BASE_URL = 'http://localhost:5000/api/v1';

// ============================================
// Cookie Utilities
// ============================================

/**
 * Get a cookie value by name
 * @param {string} name - Cookie name
 * @returns {string|null} - Cookie value or null if not found
 */
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        return parts.pop().split(';').shift();
    }
    return null;
}

/**
 * Set a cookie
 * @param {string} name - Cookie name
 * @param {string} value - Cookie value
 * @param {number} days - Days until expiration (default: 7)
 */
function setCookie(name, value, days = 7) {
    const date = new Date();
    date.setTime(date.setTime() + (days * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/`;
}

/**
 * Delete a cookie
 * @param {string} name - Cookie name
 */
function deleteCookie(name) {
    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/`;
}

// ============================================
// Authentication Check
// ============================================

/**
 * Check if user is authenticated (has valid token)
 * @returns {boolean}
 */
function isAuthenticated() {
    const token = getCookie('token');
    return token !== null && token !== '';
}

/**
 * Get the current authentication token
 * @returns {string|null}
 */
function getToken() {
    return getCookie('token');
}

/**
 * Check authentication and redirect if needed
 * Call this on pages that require authentication
 */
function checkAuthentication() {
    if (!isAuthenticated()) {
        window.location.href = 'index.html';
    }
}

// ============================================
// Login Form Handler
// ============================================

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Check if we're on the login page
    const loginForm = document.getElementById('login-form');
    
    if (loginForm) {
        // If already authenticated, redirect to places page
        if (isAuthenticated()) {
            window.location.href = 'places.html';
            return;
        }

        // Handle login form submission
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            
            // Get form data
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const errorMessage = document.getElementById('error-message');
            
            // Hide previous errors
            errorMessage.style.display = 'none';
            
            // Disable submit button during request
            const submitButton = loginForm.querySelector('button[type="submit"]');
            submitButton.disabled = true;
            submitButton.textContent = 'Logging in...';

            try {
                // TODO: Make POST request to /api/v1/auth/login
                // Send email and password in request body
                // Expected response: { "access_token": "jwt_token_here" }
                
                const response = await fetch(`${API_BASE_URL}/auth/login`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        email: email,
                        password: password
                    })
                });

                const data = await response.json();

                if (response.ok) {
                    // TODO: Store the token in a cookie named 'token'
                    // Use setCookie() function
                    setCookie('token', data.access_token, 7);
                    
                    // TODO: Redirect to places.html
                    window.location.href = 'places.html';
                    
                } else {
                    // TODO: Display error message from API
                    // The API might return: { "error": "Invalid credentials" }
                    errorMessage.textContent = data.error || 'Login failed. Please try again.';
                    errorMessage.style.display = 'block';
                }

            } catch (error) {
                // Handle network errors
                console.error('Login error:', error);
                errorMessage.textContent = 'Network error. Please check your connection.';
                errorMessage.style.display = 'block';
            } finally {
                // Re-enable submit button
                submitButton.disabled = false;
                submitButton.textContent = 'Login';
            }
        });
    }
});

// ============================================
// Logout Handler
// ============================================

/**
 * Handle logout - clear token and redirect to login
 */
function logout() {
    deleteCookie('token');
    window.location.href = 'index.html';
}

// Add logout event listener to all logout links
document.addEventListener('DOMContentLoaded', () => {
    const logoutLinks = document.querySelectorAll('#logout-link');
    logoutLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();
            logout();
        });
    });
});
