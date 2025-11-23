# HBnB - Part 4: Front-End Web Client

This is Part 4 of the HBnB project: a simple web client that interacts with a RESTful backend API (built in Part 3) to allow users to browse and review rental places.

## Project Structure

```
holbertonschool-hbnb/
├── part4/
│   ├── BackEnd/                # All files from Part 3 (Flask API + Models)
│   │   ├── app/
│   │   ├── instance/
│   │   ├── run.py
│   │   └── seed_data.py
│   └── frontend/               # New files for Part 4
│       ├── index.html          # Homepage displaying all places
│       ├── login.html          # Simple login form
│       ├── place.html          # Dynamic page for single place
│       ├── add_review.html     # Add review form
│       ├── scripts.js          # All JavaScript functionality
│       ├── styles.css          # Complete styling
│       └── images/
│           ├── logo.png
│           ├── icon.png
│           ├── Cozy Downtown Apartment.png
│           ├── Beachfront Villa.png
│           └── Mountain Cabin Retreat.png
└── README.md
```

## Features

- Single Page Client for HBnB rentals
- JWT Authentication with Login form
- Fetch & Display Places using GET /places
- Authenticated Reviews for logged-in users
- Client-side price filtering
- Dynamic place images
- Token stored in cookies for persistence

## Technologies

- HTML5
- CSS3
- JavaScript (ES6+)
- Fetch API
- JWT Authentication
- Flask (Back-end from Part 3)
- SQLite Database

## Pages

- **index.html** - Homepage displaying all places with filtering
- **login.html** - Simple login form with email/password
- **place.html** - Dynamic page for a single place with reviews
- **add_review.html** - Form to add reviews (authenticated users only)

## Authentication Flow

1. User logs in via `login.html`
2. On success, JWT is returned and saved to cookies
3. Protected routes (e.g., adding a review) use the token in the Authorization header
4. User remains logged in across page loads
5. Logout button deletes the token from cookies

## Setup Instructions

### 1. Start Backend Server

```bash
cd part4/BackEnd
source .venv/bin/activate
python run.py
```

Backend runs at: `http://127.0.0.1:5000/`

### 2. Start Frontend Server

```bash
cd part4/frontend
python3 -m http.server 8000
```

Frontend runs at: `http://127.0.0.1:8000/`

### 3. Access Application

Open your browser: `http://127.0.0.1:8000/index.html`

## API Endpoints (Consumed)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/v1/auth/login | Authenticate user |
| GET | /api/v1/places/ | Fetch all places |
| GET | /api/v1/places/{id} | Get place details |
| GET | /api/v1/reviews/place/{place_id} | Get all reviews for place |
| POST | /api/v1/reviews/ | Add a new review (auth required) |
| GET | /api/v1/users/{id} | Get user information |

## Testing

You can test the web client with any modern browser. Make sure the Flask back-end server is running at:

```
http://127.0.0.1:5000/
```

### To test login:

```bash
curl -X POST http://127.0.0.1:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@hbnb.com", "password": "admin123"}'
```

Use the token in the browser's cookies (or inspect via DevTools).

### Test Accounts:

**Admin User:**
- Email: `admin@hbnb.com`
- Password: `admin123`

**Regular User:**
- Email: `user@hbnb.com`
- Password: `password123`

## To-Do Checklist

- [x] Build basic HTML structure
- [x] Implement JWT login flow
- [x] Fetch & render places dynamically
- [x] Render reviews
- [x] Add review (authenticated)
- [x] Client-side price filtering
- [x] Display place images
- [x] Logout functionality

## Tips

- Use `document.cookie` to manage JWT tokens
- Always check for token presence before making POST requests
- Keep all dynamic rendering inside `scripts.js` using DOM APIs
- Use `DOMContentLoaded` to initialize events
- Image filenames must match place names exactly

## Author

Holberton School Student

## License

MIT License
