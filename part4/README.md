# HBnB Evolution - Part 4: Simple Web Client

## Task 0: Design ✅ COMPLETE

This directory contains the front-end web client for the HBnB application.

### Files Created

```
part4/
├── index.html          # List of places (main page)
├── login.html          # Login form
├── place.html          # Place details page
├── add_review.html     # Add review form
├── styles.css          # Complete styling
├── images/
│   ├── logo.png        # Logo for header (placeholder)
│   └── icon.png        # Favicon (placeholder)
└── README.md           # This file
```

### Task 0 Requirements Met ✅

#### 1. Four Required Pages
- ✅ **index.html** - List of Places with place cards
- ✅ **login.html** - Login Form  
- ✅ **place.html** - Place Details
- ✅ **add_review.html** - Add Review Form

#### 2. Required Structure
**Header (all pages):**
- ✅ Application logo with class `logo`
- ✅ Login button/link with class `login-button`
- ✅ Navigation links (index.html and login.html)

**Footer (all pages):**
- ✅ Text indicating "all rights reserved"

#### 3. Required CSS Classes
- ✅ `.logo` - Header logo
- ✅ `.login-button` - Login button
- ✅ `.place-card` - Place cards in index.html
- ✅ `.details-button` - View details buttons
- ✅ `.place-details` - Place details section
- ✅ `.place-info` - Place information container
- ✅ `.review-card` - Review cards
- ✅ `.add-review` - Add review section
- ✅ `.form` - Form styling

#### 4. Fixed Parameters (EXACTLY as specified)
- ✅ Margin: 20px for place and review cards
- ✅ Padding: 10px for place and review cards
- ✅ Border: 1px solid #ddd for place and review cards
- ✅ Border Radius: 10px for place and review cards

#### 5. Data Display
**Index Page:**
- ✅ Places displayed as cards with `.place-card` class
- ✅ Each card includes: name, price per night, "View Details" button with `.details-button` class

**Place Details Page:**
- ✅ Extended information (host, price, description, amenities) using `.place-details` and `.place-info`
- ✅ Reviews displayed as cards with `.review-card` class showing comment, user name, and rating
- ✅ Button to navigate to add_review.html

#### 6. Semantic HTML5
- ✅ Uses `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`
- ✅ Proper document structure
- ✅ Valid HTML5 DOCTYPE

### Design Choices (Flexible Parameters)

- **Color Palette**: 
  - Primary: #FF5A5F (Airbnb red)
  - Secondary: #00A699 (teal)
  - Background: #f5f5f5
  
- **Font**: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif

- **Images**: Placeholder files provided (logo.png, icon.png)
  - Replace with actual logo and favicon

### W3C Validation

To validate HTML files:
1. Visit: https://validator.w3.org/#validate_by_upload
2. Upload each HTML file:
   - index.html
   - login.html
   - place.html
   - add_review.html

All files use valid HTML5 structure and should pass W3C validation.

### Viewing the Pages

Simply open any HTML file in a web browser:
```bash
# From part4 directory
firefox index.html
# or
google-chrome index.html
```

Or use Python's built-in HTTP server:
```bash
cd part4
python3 -m http.server 8000
# Then open: http://localhost:8000
```

### Notes

- This is Task 0 (Design) - **HTML and CSS only**
- No JavaScript functionality yet
- All data is static/hardcoded
- Dynamic functionality will be added in Tasks 1-5

### Next Tasks

- **Task 1**: Login functionality
- **Task 2**: Display list of places from API
- **Task 3**: Place details from API  
- **Task 4**: Add review functionality

---

**Task 0 Status**: ✅ Complete and ready for submission
