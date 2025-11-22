# Part 4 Setup Instructions

## Quick Start Guide

Follow these steps to get your web client working with your API:

### Step 1: Enable CORS in Part 3 API

1. Navigate to part3 and activate your virtual environment:
```bash
cd /home/holberton/holbertonschool-hbnb/part3
source .venv/bin/activate
```

2. Install flask-cors:
```bash
pip install flask-cors
```

3. Update requirements.txt:
```bash
echo "flask-cors==4.0.0" >> requirements.txt
```

4. Edit `app/__init__.py` to add CORS support. Add this import at the top:
```python
from flask_cors import CORS
```

5. Then add this line after creating the Flask app (around line 21, after `app = Flask(__name__)`):
```python
CORS(app)
```

The relevant section should look like this:
```python
def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Enable CORS for front-end
    CORS(app)
    
    # Load configuration
    from config import config
    app.config.from_object(config[config_name])
    # ... rest of code
```

### Step 2: Start Your API Server

```bash
# Make sure you're in part3 with venv activated
cd /home/holberton/holbertonschool-hbnb/part3
source .venv/bin/activate
python run.py
```

Your API should start on `http://localhost:5000`

### Step 3: Open the Web Client

Open a new terminal (keep the API running in the first terminal):

```bash
cd /home/holberton/holbertonschool-hbnb/part4

# Option 1: Use Python's built-in HTTP server
python3 -m http.server 8000

# Then open in browser: http://localhost:8000
```

OR

```bash
# Option 2: Open directly in browser
firefox index.html
# or
google-chrome index.html
```

### Step 4: Test the Login

1. Open the web client in your browser
2. Use these test credentials:
   - **Email**: `admin@hbnb.io`
   - **Password**: `admin1234`
3. If login succeeds, you'll be redirected to the places page

## What's Already Done

✅ HTML structure for all 4 pages
✅ Complete CSS styling
✅ Authentication JavaScript (auth.js) - FULLY IMPLEMENTED

## What You Need to Complete

The following JavaScript files have TODO comments showing what needs to be implemented:

### 📝 js/places.js
- Fetch all places from API
- Display places in a grid
- Filter places by country
- Handle clicking on a place card

### 📝 js/place-details.js  
- Get place ID from URL
- Fetch place details from API
- Display place information
- Fetch and display reviews
- Show "Add Review" button for authenticated users

### 📝 js/add-review.js
- Get place ID from URL
- Check authentication
- Handle review form submission
- Send review to API with JWT token

## File Structure

```
part4/
├── README.md              ← Project overview
├── SETUP.md              ← This file
├── index.html            ← Login page (DONE)
├── places.html           ← Places list (DONE HTML, need JS)
├── place.html            ← Place details (DONE HTML, need JS)
├── add_review.html       ← Add review form (DONE HTML, need JS)
├── css/
│   └── styles.css        ← Complete styling (DONE)
└── js/
    ├── auth.js           ← Authentication (DONE)
    ├── places.js         ← Places list logic (TODO)
    ├── place-details.js  ← Place details logic (TODO)
    └── add-review.js     ← Add review logic (TODO)
```

## Debugging Tips

### Check if API is Running
```bash
curl http://localhost:5000/api/v1/places
```

### Check Browser Console
Press F12 in your browser and look at:
- **Console tab**: For JavaScript errors
- **Network tab**: To see API requests/responses
- **Application tab**: To check if cookies are being stored

### Common Issues

**CORS Error**: "blocked by CORS policy"
- Solution: Make sure you added CORS to part3/app/__init__.py

**401 Unauthorized**: "unauthorized" or "missing token"
- Solution: Make sure you're logged in and the token cookie exists

**404 Not Found**: Endpoint not found
- Solution: Check that the API URL in JavaScript matches your actual endpoints

## Next Steps

1. Complete the TODO items in the JavaScript files
2. Test each page thoroughly
3. Add error handling where needed
4. Style improvements (optional)
5. Add loading spinners (optional)

Good luck! 🚀
