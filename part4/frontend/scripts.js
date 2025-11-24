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
    const logoutButton = document.getElementById('logout-button');

    if (loginLink) {
        if (!token) {
            loginLink.style.display = 'inline-block';
            if (logoutButton) logoutButton.style.display = 'none';
        } else {
            loginLink.style.display = 'none';
            if (logoutButton) logoutButton.style.display = 'inline-block';
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
        placeCard.className = 'card';
        placeCard.dataset.price = place.price;

        // Use place name as image filename
        const imagePath = `images/${place.name}.png`;

        placeCard.innerHTML = `
            <img src="${imagePath}" alt="${place.name}" onerror="this.style.display='none'">
            <h2>${place.name}</h2>
            <p>Price per night: $${place.price}</p>
            <button class="btn" onclick="viewPlaceDetails('${place.id}')">View Details</button>
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
    const placeCards = document.querySelectorAll('.card');

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

// ========================================
// TASK 3: Place Details Page
// ========================================

// Check if we're on the place details page
if (document.getElementById('place-details')) {
    document.addEventListener('DOMContentLoaded', () => {
        const placeId = getPlaceIdFromURL();
        if (placeId) {
            checkAuthenticationForPlaceDetails();
            fetchPlaceDetails(placeId);
        } else {
            document.getElementById('place-details').innerHTML = '<p class="error">Invalid place ID.</p>';
        }
    });
}

function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}

function checkAuthenticationForPlaceDetails() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');
    const logoutButton = document.getElementById('logout-button');
    const addReviewSection = document.getElementById('add-review');

    if (loginLink) {
        if (!token) {
            loginLink.style.display = 'inline-block';
            if (logoutButton) logoutButton.style.display = 'none';
        } else {
            loginLink.style.display = 'none';
            if (logoutButton) logoutButton.style.display = 'inline-block';
        }
    }

    if (addReviewSection) {
        if (token) {
            addReviewSection.style.display = 'block';
            // Update the review link to include place ID
            const placeId = getPlaceIdFromURL();
            const reviewLink = addReviewSection.querySelector('a');
            if (reviewLink && placeId) {
                reviewLink.href = `add_review.html?place_id=${placeId}`;
            }
        } else {
            addReviewSection.style.display = 'none';
        }
    }
}

async function fetchPlaceDetails(placeId) {
    const token = getCookie('token');
    const headers = {
        'Content-Type': 'application/json'
    };

    // Include token if available (for authenticated requests)
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/places/${placeId}`, {
            method: 'GET',
            headers: headers
        });

        if (response.ok) {
            const place = await response.json();
            await displayPlaceDetails(place);
            await fetchReviews(placeId);
        } else if (response.status === 404) {
            document.getElementById('place-details').innerHTML = '<p class="error">Place not found.</p>';
        } else {
            document.getElementById('place-details').innerHTML = '<p class="error">Failed to load place details.</p>';
        }
    } catch (error) {
        console.error('Error fetching place details:', error);
        document.getElementById('place-details').innerHTML = '<p class="error">Error loading place details. Please check if the API is running.</p>';
    }
}

async function displayPlaceDetails(place) {
    const placeDetailsSection = document.getElementById('place-details');
    placeDetailsSection.innerHTML = '';

    // Create place title
    const title = document.createElement('h1');
    title.textContent = place.name || 'Unnamed Place';
    placeDetailsSection.appendChild(title);

    // Create card container
    const card = document.createElement('div');
    card.className = 'card';

    // Add place image inside card
    const img = document.createElement('img');
    img.src = `images/${place.name}.png`;
    img.alt = place.name || 'Place image';
    img.onerror = function() { this.style.display = 'none'; };
    card.appendChild(img);

    // Fetch owner/host information if owner_id exists
    let hostName = 'Unknown';
    if (place.owner_id) {
        try {
            const userResponse = await fetch(`${API_BASE_URL}/users/${place.owner_id}`);
            if (userResponse.ok) {
                const user = await userResponse.json();
                hostName = `${user.first_name} ${user.last_name}`;
            }
        } catch (error) {
            console.error('Error fetching host info:', error);
        }
    }

    // Host
    const hostPara = document.createElement('p');
    hostPara.innerHTML = `<span class="label">Host:</span> ${hostName}`;
    card.appendChild(hostPara);

    // Price
    const pricePara = document.createElement('p');
    pricePara.innerHTML = `<span class="label">Price per night:</span> $${place.price || 'N/A'}`;
    card.appendChild(pricePara);

    // Description
    const descPara = document.createElement('p');
    descPara.innerHTML = `<span class="label">Description:</span> ${place.description || 'No description available.'}`;
    card.appendChild(descPara);

    // Amenities
    const amenitiesPara = document.createElement('p');
    if (place.amenities && place.amenities.length > 0) {
        amenitiesPara.innerHTML = `<span class="label">Amenities:</span> ${place.amenities.join(', ')}`;
    } else {
        amenitiesPara.innerHTML = `<span class="label">Amenities:</span> No amenities listed`;
    }
    card.appendChild(amenitiesPara);

    placeDetailsSection.appendChild(card);
}

async function fetchReviews(placeId) {
    try {
        const response = await fetch(`${API_BASE_URL}/reviews/place/${placeId}`);

        if (response.ok) {
            const reviews = await response.json();
            displayReviews(reviews);
        } else {
            document.getElementById('reviews-list').innerHTML = '<p>Failed to load reviews.</p>';
        }
    } catch (error) {
        console.error('Error fetching reviews:', error);
        document.getElementById('reviews-list').innerHTML = '<p>Error loading reviews.</p>';
    }
}

async function displayReviews(reviews) {
    const reviewsList = document.getElementById('reviews-list');
    const reviewsSection = document.getElementById('reviews-section');
    reviewsList.innerHTML = '';

    // Show the reviews section
    if (reviewsSection) {
        reviewsSection.style.display = 'block';
    }

    if (reviews.length === 0) {
        reviewsList.innerHTML = '<p>No reviews yet. Be the first to review!</p>';
        return;
    }

    // Fetch user information for each review
    for (const review of reviews) {
        const reviewCard = document.createElement('div');
        reviewCard.className = 'review';

        // Fetch user name
        let userName = 'Anonymous';
        if (review.user_id) {
            try {
                const userResponse = await fetch(`${API_BASE_URL}/users/${review.user_id}`);
                if (userResponse.ok) {
                    const user = await userResponse.json();
                    userName = `${user.first_name} ${user.last_name}`;
                }
            } catch (error) {
                console.error('Error fetching user info:', error);
            }
        }

        const reviewHeader = document.createElement('p');
        reviewHeader.innerHTML = `<span class="label">${userName}:</span>`;
        reviewCard.appendChild(reviewHeader);

        const reviewText = document.createElement('p');
        reviewText.textContent = review.text || 'No review text provided.';
        reviewCard.appendChild(reviewText);

        reviewsList.appendChild(reviewCard);
    }
}

// ========================================
// TASK 4: Add Review Form
// ========================================

// Check if we're on the add review page
if (document.getElementById('review-form')) {
    document.addEventListener('DOMContentLoaded', () => {
        // Check authentication first
        const token = getCookie('token');
        if (!token) {
            // Redirect unauthenticated users to index page
            window.location.href = 'index.html';
            return;
        }
        
        // Check for both place_id and id parameters
        const params = new URLSearchParams(window.location.search);
        const placeId = params.get('place_id') || params.get('id');
        
        if (!placeId) {
            document.getElementById('place-name-display').innerHTML = '<span style="color: red;">Invalid place ID.</span>';
            document.getElementById('review-form').style.display = 'none';
            return;
        }
        
        // Update back link
        const backLink = document.getElementById('back-to-place');
        if (backLink) {
            backLink.href = `place.html?id=${placeId}`;
        }
        
        // Fetch and display place name
        fetchPlaceNameForReview(placeId);
        
        // Setup form submission handler
        const reviewForm = document.getElementById('review-form');
        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            
            // Get form values
            const reviewText = document.getElementById('comment').value;
            const rating = document.getElementById('rating').value;
            
            // Disable submit button during request
            const submitButton = reviewForm.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;
            submitButton.disabled = true;
            submitButton.textContent = 'Submitting...';
            
            try {
                await submitReview(token, placeId, reviewText, rating);
            } finally {
                // Re-enable submit button
                submitButton.disabled = false;
                submitButton.textContent = originalText;
            }
        });
    });
}

async function fetchPlaceNameForReview(placeId) {
    try {
        const response = await fetch(`${API_BASE_URL}/places/${placeId}`);
        
        if (response.ok) {
            const place = await response.json();
            const displayElement = document.getElementById('place-name-display');
            if (displayElement) {
                displayElement.textContent = `Reviewing: ${place.name || 'Unnamed Place'}`;
            }
        } else {
            document.getElementById('place-name-display').innerHTML = '<span style="color: red;">Place not found.</span>';
        }
    } catch (error) {
        console.error('Error fetching place:', error);
        document.getElementById('place-name-display').innerHTML = '<span style="color: red;">Error loading place information.</span>';
    }
}

async function submitReview(token, placeId, reviewText, rating) {
    try {
        const response = await fetch(`${API_BASE_URL}/reviews/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({
                text: reviewText,
                place_id: placeId
            })
        });

        if (response.ok) {
            const data = await response.json();
            alert('Review submitted successfully!');
            
            // Clear the form
            document.getElementById('review-form').reset();
            
            // Redirect to place details page after short delay
            setTimeout(() => {
                window.location.href = `place.html?id=${placeId}`;
            }, 1500);
        } else {
            // Handle error response
            const errorData = await response.json().catch(() => ({}));
            const errorMessage = errorData.message || response.statusText || 'Failed to submit review';
            
            if (response.status === 400 && errorMessage.includes('already reviewed')) {
                alert('You have already reviewed this place.');
            } else if (response.status === 400 && errorMessage.includes('own place')) {
                alert('You cannot review your own place.');
            } else if (response.status === 401) {
                alert('Your session has expired. Please login again.');
                window.location.href = 'login.html';
            } else {
                alert('Failed to submit review: ' + errorMessage);
            }
        }
    } catch (error) {
        console.error('Error submitting review:', error);
        alert('Network error. Please check if the API server is running.');
    }
}
