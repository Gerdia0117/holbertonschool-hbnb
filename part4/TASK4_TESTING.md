# Task 4 Testing Guide - Add Review Form

## Overview
Task 4 implements the review submission form with authentication, validation, and proper error handling.

## Features Implemented

### 1. Authentication Check
- Checks for JWT token on page load
- Redirects unauthenticated users to index.html
- Stores token for API requests

### 2. Place ID Validation
- Extracts place_id from URL parameters
- Shows error message if missing
- Updates "Back to Place" link with place ID

### 3. Form Submission
- Prevents default form behavior
- Gets review text and rating from form
- Shows "Submitting..." state during request
- Includes JWT token in Authorization header

### 4. API Request
- POST to `/api/v1/reviews/`
- Sends `text` and `place_id` in JSON body
- Includes `Authorization: Bearer {token}` header

### 5. Response Handling
- **Success**: Alert message, form reset, redirect to place details
- **Errors**: Specific messages for different error types:
  - Already reviewed this place
  - Cannot review own place
  - Session expired (redirect to login)
  - Other errors with message

## Testing Steps

### Test 1: Unauthenticated Access

1. **Logout** (click logout button)

2. **Try to access add review page directly**:
   ```
   http://localhost:8000/add_review.html?place_id=db5f8b89-128d-4ca8-8d33-013e93c25307
   ```

3. **Expected Result**:
   - Immediately redirected to `index.html`
   - Cannot access review form without login

### Test 2: Submit Review as Regular User (Success)

1. **Login as regular user**:
   - Go to `http://localhost:8000/login.html`
   - Email: `user@hbnb.com`
   - Password: `password123`

2. **Go to index page** and click "View Details" on any place

3. **Click "Write a Review"**

4. **Fill out the form**:
   - Rating: Select any rating (e.g., "5 - Excellent")
   - Review: "This is a test review from regular user!"

5. **Click "Submit Review"**

6. **Expected Result**:
   - Button shows "Submitting..." briefly
   - Alert: "Review submitted successfully!"
   - Form clears
   - After 1.5 seconds, redirects to place details page
   - Your new review appears in the reviews section

### Test 3: Try to Review Same Place Twice

1. **Still logged in as user@hbnb.com**

2. **Go back to the same place** and click "Write a Review" again

3. **Try to submit another review**

4. **Expected Result**:
   - Alert: "You have already reviewed this place."
   - Form not cleared
   - Stays on review form page

### Test 4: Try to Review Own Place

1. **Logout and login as admin**:
   - Email: `admin@hbnb.com`
   - Password: `admin123`

2. **Try to review any of the 3 places** (all owned by admin)

3. **Fill and submit the form**

4. **Expected Result**:
   - Alert: "You cannot review your own place."
   - Form not cleared

### Test 5: Invalid Place ID

1. **While logged in, go to**:
   ```
   http://localhost:8000/add_review.html?place_id=fake-id-123
   ```

2. **Expected Result**:
   - Page loads
   - Shows: "Place not found." in red
   - Form still visible and can be submitted
   - Will get error from API

### Test 6: Missing Place ID

1. **While logged in, go to**:
   ```
   http://localhost:8000/add_review.html
   ```

2. **Expected Result**:
   - Shows: "Invalid place ID." in red
   - Form is hidden

### Test 7: Network Error (Backend Down)

1. **Stop the backend server**:
   ```bash
   pkill -f "python.*run.py"
   ```

2. **Try to submit a review**

3. **Expected Result**:
   - Alert: "Network error. Please check if the API server is running."

4. **Restart backend**:
   ```bash
   cd part4/BackEnd
   source .venv/bin/activate
   nohup python run.py > /tmp/backend.log 2>&1 &
   ```

## API Endpoint Used

**POST /api/v1/reviews/**

Request:
```json
{
  "text": "Review text here",
  "place_id": "place-uuid-here"
}
```

Headers:
```
Content-Type: application/json
Authorization: Bearer {jwt_token}
```

Response (Success - 201):
```json
{
  "id": "review-uuid",
  "text": "Review text here",
  "user_id": "user-uuid",
  "place_id": "place-uuid"
}
```

Response (Error - 400):
```json
{
  "message": "Error message"
}
```

Common error messages:
- "You have already reviewed this place"
- "You cannot review your own place"
- "Valid place_id is required"
- "Review text is required"

## JavaScript Functions Added

### In add_review.html Page Handler
```javascript
// Check authentication on page load
const token = getCookie('token');
if (!token) {
    window.location.href = 'index.html';
    return;
}

// Get place ID from URL
const params = new URLSearchParams(window.location.search);
const placeId = params.get('place_id') || params.get('id');

// Setup form submission
reviewForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    // Get form values and submit
});
```

### `submitReview(token, placeId, reviewText, rating)`
- Makes POST request to reviews endpoint
- Includes JWT token in Authorization header
- Sends review data as JSON
- Handles success and various error cases
- Clears form and redirects on success

## User Stories Covered

✅ As an authenticated user, I can submit a review for a place  
✅ As an unauthenticated user, I am redirected when trying to access the review form  
✅ As a user, I cannot review the same place twice  
✅ As a place owner, I cannot review my own place  
✅ As a user, I see success messages when my review is submitted  
✅ As a user, I see error messages when submission fails  
✅ As a user, I am redirected back to the place after submitting a review  

## Success Criteria ✓

- [x] Only authenticated users can access the form
- [x] Unauthenticated users redirected to index.html
- [x] Place ID extracted from URL
- [x] Place name displayed on page
- [x] Form submits with preventDefault
- [x] JWT token included in Authorization header
- [x] Review text and place_id sent to API
- [x] Success message displayed on successful submission
- [x] Form cleared after success
- [x] User redirected to place details after success
- [x] Error messages displayed for failures:
  - [x] Already reviewed
  - [x] Own place
  - [x] Session expired
  - [x] Network errors
- [x] Submit button disabled during request
- [x] Button shows "Submitting..." state

## To Create Test Reviews

If you need a second user to test with, create one via the API:

```bash
curl -X POST http://localhost:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Test",
    "last_name": "User2",
    "email": "test2@test.com",
    "password": "password123"
  }'
```

Then login with `test2@test.com` / `password123`

## All Tasks Complete! 🎉

✅ Task 0: Design (4 HTML pages with CSS)  
✅ Task 1: Login (JWT authentication)  
✅ Task 2: List places (with price filter)  
✅ Task 3: Place details (with reviews)  
✅ Task 4: Add review (with authentication and validation)
