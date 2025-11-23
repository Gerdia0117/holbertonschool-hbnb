# Task 1 - Login Testing Guide

## Setup Instructions

### 1. Start the Backend API

Open a terminal and run:

```bash
cd part4/BackEnd
source .venv/bin/activate
python run.py
```

The API should start on: `http://localhost:5000`

### 2. Open the Frontend

Open another terminal and serve the frontend:

```bash
cd part4
python3 -m http.server 8000
```

Then open in browser: `http://localhost:8000/login.html`

## Test Credentials

From your Part 3 seed data, you should have:

- **Email**: `admin@hbnb.io`
- **Password**: `admin1234`

If you need to create a user, you can use your API endpoints or check the seed data in `BackEnd/sql/seed.sql`

## Testing Checklist

### Test 1: Successful Login
1. Go to `http://localhost:8000/login.html`
2. Enter valid credentials:
   - Email: `admin@hbnb.io`
   - Password: `admin1234`
3. Click "Login"
4. **Expected**: 
   - Should redirect to `index.html`
   - Cookie `token` should be stored (check browser DevTools > Application > Cookies)

### Test 2: Failed Login - Wrong Password
1. Go to `http://localhost:8000/login.html`
2. Enter:
   - Email: `admin@hbnb.io`
   - Password: `wrongpassword`
3. Click "Login"
4. **Expected**: 
   - Alert message: "Login failed: Invalid credentials"
   - Should stay on login page

### Test 3: Failed Login - Non-existent User
1. Go to `http://localhost:8000/login.html`
2. Enter:
   - Email: `nonexistent@test.com`
   - Password: `test123`
3. Click "Login"
4. **Expected**: 
   - Alert message: "Login failed: Invalid credentials"
   - Should stay on login page

### Test 4: Network Error
1. Stop the backend API (Ctrl+C in the API terminal)
2. Go to `http://localhost:8000/login.html`
3. Try to login with any credentials
4. **Expected**: 
   - Alert message: "Network error. Please check if the API server is running."

## Verifying the JWT Token

After successful login, check if the token is stored:

1. Open browser DevTools (F12)
2. Go to **Application** tab (Chrome) or **Storage** tab (Firefox)
3. Click on **Cookies** > `http://localhost:8000`
4. You should see a cookie named `token` with a long JWT string value

## Debugging

### Check API is Running
```bash
curl http://localhost:5000/api/v1/auth/login -X POST \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@hbnb.io","password":"admin1234"}'
```

Should return:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Check CORS is Enabled
In browser console (F12), if you see CORS errors, make sure:
1. CORS is enabled in `BackEnd/app/__init__.py` (it should be)
2. The backend is running

### Common Issues

**Issue**: "Network error" alert
- **Solution**: Make sure backend API is running on port 5000

**Issue**: "Login failed: Invalid credentials"
- **Solution**: Double-check credentials or seed your database

**Issue**: CORS policy error in console
- **Solution**: Verify `flask-cors` is installed and CORS(app) is in `BackEnd/app/__init__.py`

## Task 1 Requirements Met

- [x] Event listener added to login form
- [x] preventDefault used to prevent default form submission
- [x] AJAX request made using Fetch API
- [x] POST request sent to `/api/v1/auth/login`
- [x] Content-Type header set to `application/json`
- [x] Email and password sent in JSON format
- [x] JWT token stored in cookie on success
- [x] User redirected to index.html on success
- [x] Error message displayed on failure
- [x] Loading state shown during request

## Next Steps

After Task 1 is working:
- Task 2: Implement places list with API
- Task 3: Implement place details with API
- Task 4: Implement add review functionality
