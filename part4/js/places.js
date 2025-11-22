// ==================================
// Places List Page Logic
// ==================================

// Import authentication functions
// Note: Make sure auth.js is loaded before this script
// Or copy the necessary functions here

const API_BASE_URL = 'http://localhost:5000/api/v1';

// Store all places globally for filtering
let allPlaces = [];

// ============================================
// Check Authentication on Page Load
// ============================================

document.addEventListener('DOMContentLoaded', async () => {
    // TODO: Check if user is authenticated
    // If not authenticated, redirect to index.html
    // Hint: Use the checkAuthentication() function from auth.js or check cookie
    
    const token = getCookie('token');
    if (!token) {
        window.location.href = 'index.html';
        return;
    }

    // Load places when page loads
    await loadPlaces();
    
    // Set up country filter
    setupFilters();
});

// ============================================
// Utility: Get Cookie (copied from auth.js for standalone use)
// ============================================

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        return parts.pop().split(';').shift();
    }
    return null;
}

// ============================================
// Fetch and Display Places
// ============================================

/**
 * Fetch all places from the API and display them
 */
async function loadPlaces() {
    const placesContainer = document.getElementById('places-list');
    
    try {
        // TODO: Fetch places from API
        // Endpoint: GET /api/v1/places
        // You may or may not need authentication for this endpoint
        // Check your Part 3 API to see if this endpoint requires a token
        
        const response = await fetch(`${API_BASE_URL}/places`);
        
        if (!response.ok) {
            throw new Error('Failed to fetch places');
        }

        const places = await response.json();
        
        // TODO: Store places in global variable for filtering
        allPlaces = places;
        
        // TODO: Display the places
        displayPlaces(places);
        
    } catch (error) {
        console.error('Error loading places:', error);
        placesContainer.innerHTML = '<p class="error-message">Failed to load places. Please try again later.</p>';
    }
}

/**
 * Display places in the grid
 * @param {Array} places - Array of place objects
 */
function displayPlaces(places) {
    const placesContainer = document.getElementById('places-list');
    
    // TODO: Clear the loading message
    placesContainer.innerHTML = '';
    
    // TODO: Check if there are no places
    if (places.length === 0) {
        placesContainer.innerHTML = '<p class="no-results">No places found.</p>';
        return;
    }
    
    // TODO: Loop through places and create HTML for each
    places.forEach(place => {
        const placeCard = createPlaceCard(place);
        placesContainer.appendChild(placeCard);
    });
}

/**
 * Create HTML element for a place card
 * @param {Object} place - Place object from API
 * @returns {HTMLElement} - Place card element
 */
function createPlaceCard(place) {
    // TODO: Create a card element for the place
    // Include: image (placeholder if none), title, price, location
    // Make it clickable to go to place details page
    
    const card = document.createElement('div');
    card.className = 'place-card';
    
    // TODO: Add click handler to navigate to place details
    card.addEventListener('click', () => {
        window.location.href = `place.html?id=${place.id}`;
    });
    
    // TODO: Build the card HTML
    // Adjust property names based on your API response structure
    card.innerHTML = `
        <img src="${place.image_url || 'https://via.placeholder.com/400x300?text=No+Image'}" 
             alt="${place.title || place.name}"
             onerror="this.src='https://via.placeholder.com/400x300?text=No+Image'">
        <div class="place-card-content">
            <h3>${place.title || place.name}</h3>
            <p class="price">$${place.price_per_night || place.price} / night</p>
            <p class="location">📍 ${place.city || place.location}, ${place.country}</p>
        </div>
    `;
    
    return card;
}

// ============================================
// Country Filter
// ============================================

/**
 * Set up the country filter dropdown
 */
function setupFilters() {
    // TODO: Get unique countries from all places
    const countries = getUniqueCountries(allPlaces);
    
    // TODO: Populate the country filter dropdown
    const countryFilter = document.getElementById('country-filter');
    
    countries.forEach(country => {
        const option = document.createElement('option');
        option.value = country;
        option.textContent = country;
        countryFilter.appendChild(option);
    });
    
    // TODO: Add event listener for filter change
    countryFilter.addEventListener('change', (event) => {
        filterPlacesByCountry(event.target.value);
    });
}

/**
 * Get unique countries from places array
 * @param {Array} places - Array of place objects
 * @returns {Array} - Array of unique country names
 */
function getUniqueCountries(places) {
    // TODO: Extract unique countries from places
    // Return sorted array of country names
    
    const countries = places.map(place => place.country);
    const uniqueCountries = [...new Set(countries)];
    return uniqueCountries.sort();
}

/**
 * Filter places by selected country
 * @param {string} country - Country name to filter by (empty string = all)
 */
function filterPlacesByCountry(country) {
    // TODO: Filter places based on selected country
    // If country is empty string, show all places
    // Otherwise, show only places from that country
    
    let filteredPlaces;
    
    if (country === '') {
        // Show all places
        filteredPlaces = allPlaces;
    } else {
        // Filter by country
        filteredPlaces = allPlaces.filter(place => place.country === country);
    }
    
    // TODO: Re-display the filtered places
    displayPlaces(filteredPlaces);
}

// ============================================
// Price Formatting (Optional Enhancement)
// ============================================

/**
 * Format price with currency symbol
 * @param {number} price - Price value
 * @returns {string} - Formatted price string
 */
function formatPrice(price) {
    return `$${parseFloat(price).toFixed(2)}`;
}
