# HBnB Evolution - Part 4: Simple Web Client

This directory contains the complete front-end web client for the HBnB application with full backend integration.

## Project Structure

```
part4/
├── BackEnd/                    # API Backend (from Part 3)
│   ├── app/
│   ├── instance/
│   ├── run.py
│   └── seed_data.py
│
└── frontend/                   # Frontend Web Client
    ├── index.html              # List of places (main page)
    ├── login.html              # Login form
    ├── place.html              # Place details page
    ├── add_review.html         # Add review form
    ├── scripts.js              # All JavaScript functionality
    ├── styles.css              # Complete styling
    └── images/
        ├── logo.png
        ├── icon.png
        ├── Cozy Downtown Apartment.png
        ├── Beachfront Villa.png
        └── Mountain Cabin Retreat.png
```

## Prerequisites

- Python 3.x
- Flask and dependencies (see BackEnd/requirements.txt)
- Modern web browser (Chrome, Firefox, Safari)

## Setup Instructions

### 1. Setup Backend

```bash
# Navigate to backend directory
cd part4/BackEnd

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
python init_db.py

# Seed test data (creates 3 places, 2 users, reviews)
python seed_data.py
```

### 2. Start Backend Server

```bash
# From BackEnd directory with venv activated
python run.py
```

Backend will run on: http://localhost:5000

### 3. Start Frontend Server

Open a new terminal:

```bash
cd part4/frontend
python3 -m http.server 8000
```

Frontend will run on: http://localhost:8000

### 4. Access the Application

Open your browser and navigate to:
```
http://localhost:8000/index.html
```

## Test Accounts

The seed_data.py script creates these accounts:

**Admin User:**
- Email: admin@hbnb.com
- Password: admin123
- Role: Admin (owns all 3 places)

**Regular User:**
- Email: user@hbnb.com
- Password: password123
- Role: Regular user (can review places)

## Features Implemented

### Task 0: Design
- Four HTML pages with semantic structure
- CSS styling with required classes and fixed parameters
- Responsive layout
- All pages pass W3C validation

### Task 1: Login
- User authentication with JWT tokens
- Token stored in browser cookies
- Session management (login/logout)
- Redirect to index page after login

### Task 2: List of Places
- Fetch places from API endpoint
- Display places dynamically as cards
- Client-side price filtering
- Place images displayed
- Login link visibility based on authentication

### Task 3: Place Details
- Extract place ID from URL parameters
- Fetch and display place information
- Fetch and display reviews with user names
- Show "Add Review" button only for authenticated users
- Display place images

### Task 4: Add Review
- Authentication required (redirects if not logged in)
- Form submission with JWT token
- POST request to reviews API endpoint
- Success and error handling
- Redirect back to place after submission
- Prevents reviewing same place twice
- Prevents reviewing own places

## API Endpoints Used

### Authentication
- POST /api/v1/auth/login - User login

### Places
- GET /api/v1/places/ - List all places
- GET /api/v1/places/{id} - Get place details

### Reviews
- GET /api/v1/reviews/place/{place_id} - Get reviews for a place
- POST /api/v1/reviews/ - Create a new review (requires auth)

### Users
- GET /api/v1/users/{id} - Get user information

## Key Technologies

**Frontend:**
- HTML5
- CSS3
- Vanilla JavaScript (ES6+)
- Fetch API for AJAX requests
- URLSearchParams for URL handling
- Cookie-based session management

**Backend:**
- Flask
- Flask-RESTX
- Flask-JWT-Extended
- SQLAlchemy
- SQLite database

## Project Features

**Authentication:**
- JWT-based authentication
- Secure password hashing
- Cookie storage with expiration
- Protected routes

**Dynamic Content:**
- All data loaded from API
- Real-time filtering
- DOM manipulation
- Asynchronous requests

**User Experience:**
- Loading states
- Error messages
- Success notifications
- Form validation
- Responsive design

## Common Issues and Solutions

**Backend not responding:**
- Check if backend server is running on port 5000
- Verify virtual environment is activated
- Check for port conflicts

**Frontend not loading:**
- Ensure you're accessing http://localhost:8000 (not file://)
- Check browser console for errors
- Verify frontend server is running

**Login issues:**
- Clear browser cookies
- Check credentials match test accounts
- Verify backend database is seeded

**CORS errors:**
- Backend has CORS enabled for all origins
- Ensure using correct API base URL

## File Descriptions

**Frontend Files:**
- `index.html` - Main page with place listings
- `login.html` - Login form page
- `place.html` - Individual place details page
- `add_review.html` - Review submission form
- `scripts.js` - All JavaScript functionality (login, API calls, DOM manipulation)
- `styles.css` - Complete styling for all pages

**Backend Files:**
- `run.py` - Application entry point
- `init_db.py` - Database initialization
- `seed_data.py` - Test data creation
- `app/` - Application code (models, routes, business logic)

## Development Notes

**Adding New Places:**
1. Use the seed_data.py script or create via API
2. Add corresponding image to frontend/images/
3. Image filename must match place name exactly

**Modifying Styles:**
- All styles in styles.css
- Required CSS classes must not be modified
- Fixed parameters (margin, padding, border) must remain as specified

**JavaScript Organization:**
- Cookie utilities (lines 5-29)
- Login functionality (lines 32-100)
- Index page - place listing (lines 103-204)
- Place details page (lines 207-402)
- Add review form (lines 404-528)

## Testing

**Manual Testing:**
1. Login with both test accounts
2. Browse places on index page
3. Use price filter
4. View place details
5. Submit reviews (as regular user)
6. Try to review same place twice (should fail)
7. Try to review as admin (should fail - owns places)
8. Logout and verify login link appears

**Verification:**
- All pages load without errors
- API requests succeed
- Images display correctly
- Authentication works properly
- Form submissions successful
- Error messages display appropriately

## Notes

- All 4 tasks are complete and functional
- Frontend and backend are fully integrated
- Application follows RESTful API principles
- Code is organized and commented
- Error handling is comprehensive
- Security best practices implemented

## Credits

Holberton School - HBnB Evolution Project Part 4
