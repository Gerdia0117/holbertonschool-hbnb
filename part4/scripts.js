// API Configuration
const API_BASE_URL = 'http://localhost:5000/api/v1';

// Cookie utility functions
function setCookie(name, value, days = 7) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

function getCookie(name) {
    const nameEQ = name + "=";
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i];
        while (cookie.charAt(0) === ' ') {
            cookie = cookie.substring(1, cookie.length);
        }
        if (cookie.indexOf(nameEQ) === 0) {
            return cookie.substring(nameEQ.length, cookie.length);
        }
    }
    return null;
}

function deleteCookie(name) {
    document.cookie = name + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}

// Login functionality
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            // Disable submit button during request
            const submitButton = loginForm.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;
            submitButton.disabled = true;
            submitButton.textContent = 'Logging in...';
            
            try {
                await loginUser(email, password);
            } catch (error) {
                console.error('Login error:', error);
            } finally {
                // Re-enable submit button
                submitButton.disabled = false;
                submitButton.textContent = originalText;
            }
        });
    }
});

async function loginUser(email, password) {
    try {
        const response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        if (response.ok) {
            const data = await response.json();
            
            // Store the JWT token in a cookie
            setCookie('token', data.access_token, 7);
            
            // Redirect to main page
            window.location.href = 'index.html';
        } else {
            // Handle login failure
            const errorData = await response.json().catch(() => ({}));
            const errorMessage = errorData.message || response.statusText || 'Login failed';
            alert('Login failed: ' + errorMessage);
        }
    } catch (error) {
        alert('Network error. Please check if the API server is running.');
        console.error('Login error:', error);
    }
}

// Check authentication status
function isAuthenticated() {
    return getCookie('token') !== null;
}

// Logout functionality
function logout() {
    deleteCookie('token');
    window.location.href = 'login.html';
}

// ========================================
// TASK 2: Index Page - List of Places
// ========================================

let allPlaces = []; // Store all places for filtering

// Check authentication and load places on index page
if (document.getElementById('places')) {
    document.addEventListener('DOMContentLoaded', () => {
        checkAuthentication();
        fetchPlaces();
        setupPriceFilter();
    });
}

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (loginLink) {
        if (!token) {
            loginLink.style.display = 'inline-block';
        } else {
            loginLink.style.display = 'none';
        }
    }
}

async function fetchPlaces() {
    try {
        const response = await fetch(`${API_BASE_URL}/places`);

        if (response.ok) {
            const places = await response.json();
            allPlaces = places;
            displayPlaces(places);
        } else {
            document.getElementById('places').innerHTML = '<p class="error">Failed to load places.</p>';
        }
    } catch (error) {
        console.error('Error fetching places:', error);
        document.getElementById('places').innerHTML = '<p class="error">Error loading places. Please check if the API is running.</p>';
    }
}

function displayPlaces(places) {
    const placesContainer = document.getElementById('places');
    placesContainer.innerHTML = '';

    if (places.length === 0) {
        placesContainer.innerHTML = '<p>No places available.</p>';
        return;
    }

    places.forEach(place => {
        const placeCard = document.createElement('div');
        placeCard.className = 'place-card';
        placeCard.dataset.price = place.price;

        placeCard.innerHTML = `
            <h2>${place.name}</h2>
            <p class="price">$${place.price} per night</p>
            <p>${place.description || 'No description available'}</p>
            <button class="details-button" onclick="viewPlaceDetails('${place.id}')">View Details</button>
        `;

        placesContainer.appendChild(placeCard);
    });
}

function setupPriceFilter() {
    const priceFilter = document.getElementById('price-filter');
    
    if (priceFilter) {
        priceFilter.addEventListener('change', (event) => {
            const selectedPrice = event.target.value;
            filterPlacesByPrice(selectedPrice);
        });
    }
}

function filterPlacesByPrice(maxPrice) {
    const placeCards = document.querySelectorAll('.place-card');

    placeCards.forEach(card => {
        const price = parseFloat(card.dataset.price);

        if (maxPrice === 'all') {
            card.style.display = 'inline-block';
        } else {
            const max = parseFloat(maxPrice);
            if (price <= max) {
                card.style.display = 'inline-block';
            } else {
                card.style.display = 'none';
            }
        }
    });
}

function viewPlaceDetails(placeId) {
    window.location.href = `place.html?id=${placeId}`;
}
