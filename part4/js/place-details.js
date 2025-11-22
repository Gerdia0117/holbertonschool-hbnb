// ==================================
// Place Details Page Logic
// ==================================

const API_BASE_URL = 'http://localhost:5000/api/v1';

// Store current place ID
let currentPlaceId = null;

// ============================================
// Page Initialization
// ============================================

document.addEventListener('DOMContentLoaded', async () => {
    // TODO: Get place ID from URL parameters
    // URL format: place.html?id=PLACE_ID
    // Hint: Use URLSearchParams
    
    const urlParams = new URLSearchParams(window.location.search);
    currentPlaceId = urlParams.get('id');
    
    // TODO: Check if ID exists
    if (!currentPlaceId) {
        alert('No place ID provided');
        window.location.href = 'places.html';
        return;
    }
    
    // Load place details and reviews
    await loadPlaceDetails();
    await loadReviews();
    
    // Set up Add Review button (only show if authenticated)
    setupAddReviewButton();
});

// ============================================
// Utility: Get Cookie
// ============================================

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        return parts.pop().split(';').shift();
    }
    return null;
}

function isAuthenticated() {
    return getCookie('token') !== null;
}

// ============================================
// Load Place Details
// ============================================

/**
 * Fetch and display details for the current place
 */
async function loadPlaceDetails() {
    const detailsContainer = document.getElementById('place-details');
    
    try {
        // TODO: Fetch place details from API
        // Endpoint: GET /api/v1/places/:id
        
        const response = await fetch(`${API_BASE_URL}/places/${currentPlaceId}`);
        
        if (!response.ok) {
            throw new Error('Failed to fetch place details');
        }
        
        const place = await response.json();
        
        // TODO: Display the place details
        displayPlaceDetails(place);
        
    } catch (error) {
        console.error('Error loading place details:', error);
        detailsContainer.innerHTML = '<p class="error-message">Failed to load place details.</p>';
    }
}

/**
 * Display place details on the page
 * @param {Object} place - Place object from API
 */
function displayPlaceDetails(place) {
    const detailsContainer = document.getElementById('place-details');
    
    // TODO: Build HTML for place details
    // Include: title, price, location, description, owner, amenities, etc.
    // Adjust property names based on your API response structure
    
    const amenitiesHTML = place.amenities && place.amenities.length > 0
        ? place.amenities.map(amenity => `<span class="amenity-tag">${amenity.name || amenity}</span>`).join('')
        : '<p>No amenities listed</p>';
    
    detailsContainer.innerHTML = `
        <div class="place-header">
            <h2>${place.title || place.name}</h2>
            <p class="place-price">$${place.price_per_night || place.price} per night</p>
            <p class="place-location">📍 ${place.city || place.location}, ${place.country}</p>
            <p class="place-owner">Host: ${place.owner ? place.owner.first_name + ' ' + place.owner.last_name : 'N/A'}</p>
        </div>
        
        <div class="place-description">
            <h3>Description</h3>
            <p>${place.description || 'No description available'}</p>
        </div>
        
        <div class="place-amenities">
            <h3>Amenities</h3>
            <div class="amenities-list">
                ${amenitiesHTML}
            </div>
        </div>
    `;
}

// ============================================
// Load Reviews
// ============================================

/**
 * Fetch and display reviews for the current place
 */
async function loadReviews() {
    const reviewsContainer = document.getElementById('reviews-list');
    
    try {
        // TODO: Fetch reviews from API
        // Endpoint might be: GET /api/v1/places/:id/reviews
        // OR: GET /api/v1/reviews?place_id=:id
        // Check your Part 3 API documentation
        
        const response = await fetch(`${API_BASE_URL}/places/${currentPlaceId}/reviews`);
        
        if (!response.ok) {
            throw new Error('Failed to fetch reviews');
        }
        
        const reviews = await response.json();
        
        // TODO: Display reviews
        displayReviews(reviews);
        
    } catch (error) {
        console.error('Error loading reviews:', error);
        reviewsContainer.innerHTML = '<p class="no-reviews">Unable to load reviews.</p>';
    }
}

/**
 * Display reviews on the page
 * @param {Array} reviews - Array of review objects
 */
function displayReviews(reviews) {
    const reviewsContainer = document.getElementById('reviews-list');
    
    // TODO: Check if there are no reviews
    if (!reviews || reviews.length === 0) {
        reviewsContainer.innerHTML = '<p class="no-reviews">No reviews yet. Be the first to review!</p>';
        return;
    }
    
    // TODO: Build HTML for each review
    const reviewsHTML = reviews.map(review => `
        <div class="review-card">
            <div class="review-header">
                <span class="review-author">${review.user ? review.user.first_name + ' ' + review.user.last_name : 'Anonymous'}</span>
                <span class="review-rating">${'⭐'.repeat(review.rating)}</span>
            </div>
            <p class="review-date">${formatDate(review.created_at)}</p>
            <p class="review-text">${review.text || review.comment}</p>
        </div>
    `).join('');
    
    reviewsContainer.innerHTML = reviewsHTML;
}

/**
 * Format date string to readable format
 * @param {string} dateString - ISO date string
 * @returns {string} - Formatted date
 */
function formatDate(dateString) {
    if (!dateString) return 'Date unknown';
    
    const date = new Date(dateString);
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
}

// ============================================
// Add Review Button Setup
// ============================================

/**
 * Show Add Review button only if user is authenticated
 */
function setupAddReviewButton() {
    const addReviewBtn = document.getElementById('add-review-btn');
    
    // TODO: Check if user is authenticated
    if (isAuthenticated()) {
        // Show the button
        addReviewBtn.style.display = 'block';
        
        // TODO: Add click handler to navigate to add review page
        addReviewBtn.addEventListener('click', () => {
            window.location.href = `add_review.html?place_id=${currentPlaceId}`;
        });
    } else {
        // Hide the button or show login prompt
        addReviewBtn.style.display = 'none';
    }
}
