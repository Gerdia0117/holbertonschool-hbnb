# HBnB Evolution - Part 4: Simple Web Client

## Overview
This is the front-end web client for the HBnB application. It provides an interactive user interface that connects to the REST API built in Part 3.

## Project Structure
```
part4/
├── index.html          # Login page (entry point)
├── places.html         # List of all places
├── place.html          # Detailed view of a single place
├── add_review.html     # Form to add a review
├── css/
│   └── styles.css      # Main stylesheet
├── js/
│   ├── auth.js         # Authentication utilities
│   ├── places.js       # Places list logic
│   ├── place-details.js # Place details logic
│   └── add-review.js   # Add review logic
└── images/             # Image assets
```

## Technologies Used
- **HTML5**: Structure and content
- **CSS3**: Styling and responsive design
- **JavaScript ES6**: Client-side logic and API interaction
- **Fetch API**: HTTP requests to back-end
- **Cookies**: JWT token storage for authentication

## API Endpoints (from Part 3)
Your front-end connects to these endpoints:

### Authentication
- `POST /api/v1/auth/login` - User login (returns JWT token)

### Places
- `GET /api/v1/places` - Get all places
- `GET /api/v1/places/{id}` - Get specific place details

### Reviews
- `POST /api/v1/reviews` - Create a new review (requires authentication)
- `GET /api/v1/places/{id}/reviews` - Get reviews for a place

## Setup Instructions

### 1. Enable CORS in Part 3 API
Before running the client, you need to enable CORS in your API:

```bash
# Navigate to Part 3
cd ../part3

# Activate virtual environment
source .venv/bin/activate

# Install flask-cors
pip install flask-cors

# Update requirements.txt
echo "flask-cors==4.0.0" >> requirements.txt
```

Then add CORS configuration to `part3/app/__init__.py` (see instructions below).

### 2. Start the API Server
```bash
# From part3 directory with venv activated
python run.py
```

The API should run on `http://localhost:5000`

### 3. Open the Web Client
Simply open `index.html` in your web browser:
```bash
# From part4 directory
firefox index.html
# or
google-chrome index.html
# or just double-click index.html in your file manager
```

## Usage Flow

1. **Login** (`index.html`)
   - Enter email and password
   - On success, JWT token is stored in a cookie
   - Redirected to places list

2. **Places List** (`places.html`)
   - View all places
   - Filter by country
   - Click on a place to see details

3. **Place Details** (`place.html`)
   - View full information about a place
   - See reviews
   - Click "Add Review" if authenticated

4. **Add Review** (`add_review.html`)
   - Rate the place (1-5 stars)
   - Write review text
   - Submit to API

## Authentication
- JWT tokens are stored as cookies with the name `token`
- Protected pages check for token existence
- If no token found, user is redirected to login page
- Token is sent in `Authorization: Bearer <token>` header for API requests

## Testing
Test user credentials (from Part 3 seed data):
- **Email**: admin@hbnb.io
- **Password**: admin1234

## Development Notes
- All API calls use `http://localhost:5000` as base URL
- You can change this in each JS file if your API runs on a different port
- The client uses vanilla JavaScript (no frameworks)
- All files use ES6+ syntax

## Troubleshooting

### CORS Error
If you get "CORS policy" errors in browser console:
- Make sure flask-cors is installed in Part 3
- Verify CORS is configured in `app/__init__.py`
- Restart your API server

### Token Issues
If pages keep redirecting to login:
- Check browser console for errors
- Verify token is being stored (browser DevTools > Application > Cookies)
- Ensure login API is returning a valid JWT token

### API Connection Failed
- Verify Part 3 API is running (`http://localhost:5000`)
- Check API endpoints match what's in your JavaScript files
- Use browser Network tab to inspect failed requests

## Next Steps
- Implement all TODO items in JavaScript files
- Style pages according to design specifications
- Add error handling and loading states
- Test with different users and edge cases
