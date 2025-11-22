# 🚀 Quick Start Guide - Part 4

## You're Ready to Go!

Everything is set up! Here's how to start:

## Step 1: Start Your API (Terminal 1)

```bash
cd ~/holbertonschool-hbnb/part3
source .venv/bin/activate
python run.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

**Keep this terminal running!**

## Step 2: Open Your Web Client (New Terminal 2)

Option A - Direct browser open:
```bash
cd ~/holbertonschool-hbnb/part4
firefox index.html
```

Option B - Use a web server (recommended):
```bash
cd ~/holbertonschool-hbnb/part4
python3 -m http.server 8000
```
Then open: http://localhost:8000

## Step 3: Test Login

**Test credentials:**
- Email: `admin@hbnb.io`
- Password: `admin1234`

If login works → You'll be redirected to the places page!

## What Works Right Now

✅ **Login page** - Fully working
✅ **Authentication** - Token storage in cookies
✅ **Logout** - Working on all pages
✅ **Places list** - Should work (may need minor tweaks based on your API response structure)
✅ **Place details** - Should work (may need minor tweaks)
✅ **Add review** - Should work (may need minor tweaks)

## Testing Checklist

1. ☐ Login with admin credentials
2. ☐ See list of places
3. ☐ Filter places by country
4. ☐ Click on a place to see details
5. ☐ View reviews for a place
6. ☐ Click "Add Review" button
7. ☐ Submit a review
8. ☐ Logout

## Debugging

### Open Browser Console (F12)

Check three tabs:
1. **Console** - For JavaScript errors
2. **Network** - To see API requests/responses
3. **Application → Cookies** - To verify token is stored

### Common Fixes Needed

The JavaScript files have some assumptions about your API response structure. You might need to adjust property names:

**In `js/places.js`:**
- Line 128-136: Check if your API returns `title` or `name`, `price_per_night` or `price`, etc.

**In `js/place-details.js`:**
- Line 102-118: Adjust property names to match your API response

**In `js/add-review.js`:**
- Line 169: Check if review field is called `text` or `comment` in your API

### Check Your API Response Format

Test your API manually:
```bash
# Get all places
curl http://localhost:5000/api/v1/places

# Get specific place
curl http://localhost:5000/api/v1/places/YOUR_PLACE_ID

# Login (get token)
curl -X POST http://localhost:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@hbnb.io","password":"admin1234"}'
```

## Need Help?

1. Read `README.md` for project overview
2. Read `SETUP.md` for detailed setup instructions
3. Check console errors in browser (F12)
4. Verify API is running on port 5000
5. Make sure CORS is enabled (you should see no CORS errors in console)

## File Structure Reference

```
part4/
├── QUICKSTART.md         ← You are here!
├── SETUP.md             ← Detailed setup
├── README.md            ← Project overview
├── index.html           ← Login page
├── places.html          ← Places list
├── place.html           ← Place details
├── add_review.html      ← Add review
├── css/
│   └── styles.css       ← All styling
└── js/
    ├── auth.js          ← Login/logout (DONE ✅)
    ├── places.js        ← Places list (mostly done)
    ├── place-details.js ← Place details (mostly done)
    └── add-review.js    ← Add review (mostly done)
```

Good luck! 🎉
