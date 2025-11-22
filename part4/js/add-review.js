// ==================================
// Add Review Page Logic
// ==================================

const API_BASE_URL = 'http://localhost:5000/api/v1';

// Store current place ID
let currentPlaceId = null;

// ============================================
// Page Initialization
// ============================================

document.addEventListener('DOMContentLoaded', async () => {
    // TODO: Check authentication first
    // If not authenticated, redirect to login page
    if (!isAuthenticated()) {
        alert('You must be logged in to add a review');
        window.location.href = 'index.html';
        return;
    }
    
    // TODO: Get place_id from URL parameters
    const urlParams = new URLSearchParams(window.location.search);
    currentPlaceId = urlParams.get('place_id');
    
    // Check if place_id exists
    if (!currentPlaceId) {
        alert('No place specified');
        window.location.href = 'places.html';
        return;
    }
    
    // Load place information to show which place is being reviewed
    await loadPlaceInfo();
    
    // Set up back link
    setupBackLink();
    
    // Handle form submission
    setupFormHandler();
});

// ============================================
// Utility Functions
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

function getToken() {
    return getCookie('token');
}

// ============================================
// Load Place Information
// ============================================

/**
 * Fetch basic place info to show which place is being reviewed
 */
async function loadPlaceInfo() {
    const placeInfoContainer = document.getElementById('place-info');
    
    try {
        // TODO: Fetch place details
        const response = await fetch(`${API_BASE_URL}/places/${currentPlaceId}`);
        
        if (!response.ok) {
            throw new Error('Failed to fetch place info');
        }
        
        const place = await response.json();
        
        // Display place name
        placeInfoContainer.innerHTML = `
            <h3>Reviewing: ${place.title || place.name}</h3>
            <p>${place.city || place.location}, ${place.country}</p>
        `;
        
    } catch (error) {
        console.error('Error loading place info:', error);
        placeInfoContainer.innerHTML = '<p>Place information unavailable</p>';
    }
}

// ============================================
// Setup Back Link
// ============================================

/**
 * Set up the back link to return to place details
 */
function setupBackLink() {
    const backLink = document.getElementById('back-link');
    backLink.href = `place.html?id=${currentPlaceId}`;
}

// ============================================
// Form Submission Handler
// ============================================

/**
 * Set up form submission handler
 */
function setupFormHandler() {
    const reviewForm = document.getElementById('review-form');
    
    reviewForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        
        // Get form data
        const rating = document.getElementById('rating').value;
        const reviewText = document.getElementById('review-text').value;
        
        // Get message elements
        const errorMessage = document.getElementById('error-message');
        const successMessage = document.getElementById('success-message');
        
        // Hide previous messages
        errorMessage.style.display = 'none';
        successMessage.style.display = 'none';
        
        // Validate
        if (!rating) {
            errorMessage.textContent = 'Please select a rating';
            errorMessage.style.display = 'block';
            return;
        }
        
        if (reviewText.length < 10) {
            errorMessage.textContent = 'Review must be at least 10 characters';
            errorMessage.style.display = 'block';
            return;
        }
        
        // Disable submit button
        const submitButton = reviewForm.querySelector('button[type="submit"]');
        submitButton.disabled = true;
        submitButton.textContent = 'Submitting...';
        
        try {
            // TODO: Submit review to API
            // Endpoint: POST /api/v1/reviews
            // Required fields: place_id, rating, text (or comment)
            // Must include Authorization header with JWT token
            
            const token = getToken();
            
            const response = await fetch(`${API_BASE_URL}/reviews`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    place_id: currentPlaceId,
                    rating: parseInt(rating),
                    text: reviewText  // Or 'comment' depending on your API
                })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                // TODO: Show success message
                successMessage.textContent = 'Review submitted successfully!';
                successMessage.style.display = 'block';
                
                // TODO: Redirect back to place details after 2 seconds
                setTimeout(() => {
                    window.location.href = `place.html?id=${currentPlaceId}`;
                }, 2000);
                
            } else {
                // TODO: Show error message from API
                errorMessage.textContent = data.error || data.message || 'Failed to submit review';
                errorMessage.style.display = 'block';
            }
            
        } catch (error) {
            console.error('Error submitting review:', error);
            errorMessage.textContent = 'Network error. Please try again.';
            errorMessage.style.display = 'block';
        } finally {
            // Re-enable submit button
            submitButton.disabled = false;
            submitButton.textContent = 'Submit Review';
        }
    });
}
