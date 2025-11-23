# Task 3 Testing Guide - Place Details

## Overview
Task 3 implements the place details page with dynamic content loaded from the API.

## Features Implemented

### 1. Get Place ID from URL
- Extracts `id` parameter from URL query string
- Example: `place.html?id=138ce2ad-93d2-4b4f-b9a1-94faba43aff9`

### 2. Check Authentication
- Shows/hides login link based on JWT token
- Shows "Add Review" section only if user is authenticated
- If not logged in: "Add Review" section is hidden
- If logged in: "Add Review" section is visible

### 3. Fetch Place Details
- GET request to `/api/v1/places/{place_id}`
- Includes JWT token in Authorization header if available
- Handles 404 and other errors gracefully

### 4. Display Place Information
- **Name**: Place title
- **Host**: Fetched from `/api/v1/users/{owner_id}` (shows full name)
- **Price**: Per night
- **Description**: Full description or fallback message
- **Amenities**: List of amenities or "No amenities listed"

### 5. Fetch and Display Reviews
- GET request to `/api/v1/reviews/place/{place_id}`
- For each review, fetches user information to display reviewer name
- Shows "No reviews yet" if no reviews exist

## Testing Steps

### Test 1: View Place Without Login

1. **Clear cookies** (to ensure you're not logged in):
   - Open browser DevTools (F12)
   - Go to Application/Storage tab
   - Clear all cookies

2. **Navigate to index page**:
   ```
   http://localhost:8000/index.html
   ```

3. **Click "View Details"** on any place card

4. **Verify**:
   - Place details are displayed (name, host, price, description, amenities)
   - Reviews are displayed (if any exist)
   - "Login" link is visible in header
   - "Add Review" section is NOT visible

### Test 2: View Place With Login

1. **Login first**:
   - Go to `http://localhost:8000/login.html`
   - Email: `admin@hbnb.com`
   - Password: `admin123`

2. **Navigate to index page** and click "View Details" on a place

3. **Verify**:
   - Place details are displayed
   - Reviews are displayed
   - "Login" link is NOT visible in header
   - "Add Review" section IS visible
   - "Write a Review" button is visible

### Test 3: Direct URL with Place ID

1. **Find a place ID**:
   - Go to `http://localhost:8000/index.html`
   - Open browser DevTools (F12) → Console
   - Type: `allPlaces` (this shows all loaded places)
   - Copy a place ID from the output

2. **Visit place directly**:
   ```
   http://localhost:8000/place.html?id={PLACE_ID}
   ```
   Example: `http://localhost:8000/place.html?id=138ce2ad-93d2-4b4f-b9a1-94faba43aff9`

3. **Verify**:
   - Page loads correctly
   - All place information is displayed

### Test 4: Invalid Place ID

1. **Visit with fake ID**:
   ```
   http://localhost:8000/place.html?id=fake-id-123
   ```

2. **Verify**:
   - Error message displayed: "Place not found."

### Test 5: Missing Place ID

1. **Visit without ID parameter**:
   ```
   http://localhost:8000/place.html
   ```

2. **Verify**:
   - Error message displayed: "Invalid place ID."

## API Endpoints Used

1. **GET /api/v1/places/{place_id}**
   - Returns place details
   - No authentication required

2. **GET /api/v1/users/{user_id}**
   - Returns user information (for host name)
   - No authentication required

3. **GET /api/v1/reviews/place/{place_id}**
   - Returns all reviews for a place
   - No authentication required

## JavaScript Functions Added

### `getPlaceIdFromURL()`
- Extracts place ID from URL query parameters
- Returns: place ID string or null

### `checkAuthenticationForPlaceDetails()`
- Checks for JWT token in cookies
- Shows/hides login link
- Shows/hides "Add Review" section

### `fetchPlaceDetails(placeId)`
- Fetches place data from API
- Includes Authorization header if token exists
- Calls `displayPlaceDetails()` on success

### `displayPlaceDetails(place)`
- Clears current content
- Creates DOM elements for:
  - Place title (h1)
  - Place info container (div.place-info)
    - Host (fetched from users API)
    - Price
    - Description
    - Amenities

### `fetchReviews(placeId)`
- Fetches reviews for the place
- Calls `displayReviews()` on success

### `displayReviews(reviews)`
- Clears reviews list
- For each review:
  - Fetches user information for reviewer name
  - Creates review card with user name and review text
- Shows "No reviews yet" if empty

## Known Issues / Notes

1. **Current seed data has null values**:
   - The existing place in the database has all null fields
   - You may need to create proper test data

2. **To create test data**, you can:
   - Use the API directly with curl/Postman
   - Or add seed data to the database initialization

## Browser Console Debugging

Open DevTools (F12) → Console to see:
- Fetch requests and responses
- Any errors that occur
- API endpoints being called

Example commands to try in console:
```javascript
// Check if authenticated
getCookie('token')

// Get current place ID
getPlaceIdFromURL()

// View all places (from index page)
allPlaces
```

## Success Criteria ✓

- [x] Place ID extracted from URL query parameters
- [x] Authentication check on page load
- [x] Login link shows/hides based on authentication
- [x] "Add Review" section shows only when authenticated
- [x] Place details fetched from API
- [x] JWT token included in Authorization header (if available)
- [x] Place information displayed dynamically:
  - [x] Name
  - [x] Host (fetched from users API)
  - [x] Price
  - [x] Description
  - [x] Amenities
- [x] Reviews fetched and displayed
- [x] Reviewer names fetched from users API
- [x] Error handling for invalid/missing place ID
- [x] Error handling for API failures
