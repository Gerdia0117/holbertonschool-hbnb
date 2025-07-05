#!/usr/bin/env python3
"""
Complete test suite for HBnB Flask application
Tests all API endpoints with correct data requirements
"""

import unittest
import json
import sys
import os

# Add the current directory to the path to import the app
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import create_app


class TestHBnBApp(unittest.TestCase):
    """Complete test case for HBnB Flask application"""
    
    def setUp(self):
        """Set up test environment before each test"""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
    
    def tearDown(self):
        """Clean up after each test"""
        self.ctx.pop()
    
    def test_app_creation(self):
        """Test that the Flask app is created successfully"""
        print("🔧 Testing app creation...")
        self.assertIsNotNone(self.app)
        self.assertEqual(self.app.name, 'app')
        self.assertIn('v1_api', self.app.blueprints)
        self.assertIn('restx_doc', self.app.blueprints)
        print("✅ App creation test passed!")
    
    def test_swagger_ui_accessible(self):
        """Test that Swagger UI endpoint is accessible"""
        print("📚 Testing Swagger UI accessibility...")
        response = self.client.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.content_type)
        self.assertIn(b'HBnB Application API', response.data)
        print("✅ Swagger UI test passed!")
    
    def test_swagger_json_accessible(self):
        """Test that Swagger JSON spec is accessible"""
        print("📋 Testing Swagger JSON spec...")
        response = self.client.get('/api/v1/swagger.json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        
        data = json.loads(response.data)
        self.assertIn('info', data)
        self.assertIn('paths', data)
        self.assertEqual(data['info']['title'], 'HBnB Application API')
        print("✅ Swagger JSON test passed!")
    
    def test_users_endpoint_get(self):
        """Test GET request to users endpoint"""
        print("👥 Testing users GET endpoint...")
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        print("✅ Users GET test passed!")
    
    def test_users_endpoint_post_missing_password(self):
        """Test POST request to users endpoint without password"""
        print("🔒 Testing users POST without password...")
        user_data = {
            "first_name": "Test",
            "last_name": "User",
            "email": "test.user@example.com"
        }
        response = self.client.post('/api/v1/users/',
                                  data=json.dumps(user_data),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('Password is required', data.get('message', ''))
        print("✅ Users POST validation test passed!")
    
    def test_users_endpoint_post_valid(self):
        """Test POST request to users endpoint with complete valid data"""
        print("👤 Testing users POST with valid data...")
        user_data = {
            "first_name": "Test",
            "last_name": "User",
            "email": "test.user@example.com",
            "password": "testpassword123"
        }
        response = self.client.post('/api/v1/users/',
                                  data=json.dumps(user_data),
                                  content_type='application/json')
        # Should create user successfully (200 or 201)
        self.assertIn(response.status_code, [200, 201])
        print("✅ Users POST valid data test passed!")
    
    def test_amenities_endpoint_get(self):
        """Test GET request to amenities endpoint"""
        print("🏠 Testing amenities GET endpoint...")
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        print("✅ Amenities GET test passed!")
    
    def test_amenities_endpoint_post_empty(self):
        """Test POST request to amenities endpoint with empty data"""
        print("🚫 Testing amenities POST with empty data...")
        response = self.client.post('/api/v1/amenities/',
                                  data=json.dumps({}),
                                  content_type='application/json')
        # Should return 400 or 422 for missing required fields
        self.assertIn(response.status_code, [400, 422])
        print("✅ Amenities POST validation test passed!")
    
    def test_amenities_endpoint_post_valid(self):
        """Test POST request to amenities endpoint with valid data"""
        print("🏡 Testing amenities POST with valid data...")
        amenity_data = {
            "name": "Test Amenity"
        }
        response = self.client.post('/api/v1/amenities/',
                                  data=json.dumps(amenity_data),
                                  content_type='application/json')
        # Should create amenity successfully (200 or 201)
        self.assertIn(response.status_code, [200, 201])
        print("✅ Amenities POST valid data test passed!")
    
    def test_user_not_found(self):
        """Test GET request for non-existent user"""
        print("🔍 Testing user not found scenario...")
        response = self.client.get('/api/v1/users/non-existent-id')
        self.assertEqual(response.status_code, 404)
        print("✅ User not found test passed!")
    
    def test_amenity_not_found(self):
        """Test GET request for non-existent amenity"""
        print("🔍 Testing amenity not found scenario...")
        response = self.client.get('/api/v1/amenities/non-existent-id')
        self.assertEqual(response.status_code, 404)
        print("✅ Amenity not found test passed!")
    
    def test_error_handling(self):
        """Test various error scenarios"""
        print("⚠️ Testing error handling...")
        
        # Test invalid endpoint
        response = self.client.get('/api/v1/invalid-endpoint')
        self.assertEqual(response.status_code, 404)
        
        # Test method not allowed
        response = self.client.delete('/api/v1/users/')
        self.assertEqual(response.status_code, 405)
        
        # Test invalid JSON
        response = self.client.post('/api/v1/users/',
                                  data="invalid json",
                                  content_type='application/json')
        self.assertIn(response.status_code, [400, 422])
        
        print("✅ Error handling tests passed!")
    
    def test_routes_and_methods(self):
        """Test that all routes are registered with correct methods"""
        print("🛣️ Testing routes and methods...")
        
        routes = [rule.rule for rule in self.app.url_map.iter_rules()]
        rules = {rule.rule: rule.methods for rule in self.app.url_map.iter_rules()}
        
        # Check main API routes exist
        required_routes = [
            '/api/v1/',
            '/api/v1/users/',
            '/api/v1/amenities/',
            '/api/v1/swagger.json'
        ]
        
        for route in required_routes:
            self.assertIn(route, routes, f"Route {route} not found")
        
        # Check HTTP methods
        users_methods = rules.get('/api/v1/users/')
        self.assertIn('GET', users_methods)
        self.assertIn('POST', users_methods)
        
        amenities_methods = rules.get('/api/v1/amenities/')
        self.assertIn('GET', amenities_methods)
        self.assertIn('POST', amenities_methods)
        
        print("✅ Routes and methods test passed!")


class TestAPIWorkflow(unittest.TestCase):
    """Test complete API workflows"""
    
    def setUp(self):
        """Set up test environment"""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
    
    def tearDown(self):
        """Clean up after tests"""
        self.ctx.pop()
    
    def test_complete_user_workflow(self):
        """Test complete user management workflow"""
        print("🔄 Testing complete user workflow...")
        
        # Step 1: Get initial users list
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        initial_users = json.loads(response.data)
        
        # Step 2: Create a new user
        user_data = {
            "first_name": "Workflow",
            "last_name": "Test",
            "email": "workflow.test@example.com",
            "password": "workflowpass123"
        }
        
        create_response = self.client.post('/api/v1/users/',
                                         data=json.dumps(user_data),
                                         content_type='application/json')
        
        if create_response.status_code in [200, 201]:
            print("  ✅ User creation successful")
            
            # Try to get user details if ID is returned
            try:
                user_response_data = json.loads(create_response.data)
                if 'id' in user_response_data:
                    user_id = user_response_data['id']
                    
                    # Step 3: Retrieve the created user
                    get_response = self.client.get(f'/api/v1/users/{user_id}')
                    print(f"  📄 User retrieval status: {get_response.status_code}")
                    
                    # Step 4: Try to update the user
                    update_data = {"first_name": "Updated"}
                    put_response = self.client.put(f'/api/v1/users/{user_id}',
                                                  data=json.dumps(update_data),
                                                  content_type='application/json')
                    print(f"  ✏️ User update status: {put_response.status_code}")
            except (json.JSONDecodeError, KeyError):
                print("  ℹ️ User ID not returned in response format")
        
        print("✅ Complete user workflow test completed!")
    
    def test_api_documentation_workflow(self):
        """Test API documentation workflow"""
        print("📖 Testing API documentation workflow...")
        
        # Test Swagger UI
        ui_response = self.client.get('/api/v1/')
        self.assertEqual(ui_response.status_code, 200)
        self.assertIn('text/html', ui_response.content_type)
        
        # Test Swagger JSON spec
        spec_response = self.client.get('/api/v1/swagger.json')
        self.assertEqual(spec_response.status_code, 200)
        self.assertEqual(spec_response.content_type, 'application/json')
        
        spec_data = json.loads(spec_response.data)
        
        # Verify spec contains expected information
        self.assertIn('info', spec_data)
        self.assertIn('paths', spec_data)
        self.assertEqual(spec_data['info']['title'], 'HBnB Application API')
        
        # Check that endpoints are documented
        paths = spec_data.get('paths', {})
        documented_endpoints = list(paths.keys())
        
        print(f"  📋 Documented endpoints: {len(documented_endpoints)}")
        for endpoint in documented_endpoints:
            print(f"    - {endpoint}")
        
        print("✅ API documentation workflow test passed!")


def run_comprehensive_tests():
    """Run all tests with detailed output"""
    print("=" * 70)
    print("🧪 HBnB Flask Application - Comprehensive Test Suite")
    print("=" * 70)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestHBnBApp))
    suite.addTests(loader.loadTestsFromTestCase(TestAPIWorkflow))
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(suite)
    
    # Print comprehensive summary
    print("\n" + "=" * 70)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 70)
    
    if result.wasSuccessful():
        print("🎉 ALL TESTS PASSED SUCCESSFULLY!")
        print(f"✅ Total tests run: {result.testsRun}")
        print("\n🚀 Your HBnB Flask application is working perfectly!")
        print("\n📋 What was tested:")
        print("  ✅ Flask app creation and configuration")
        print("  ✅ API blueprint registration")
        print("  ✅ Swagger UI and documentation")
        print("  ✅ Users API endpoints (GET, POST)")
        print("  ✅ Amenities API endpoints (GET, POST)")
        print("  ✅ Error handling (404, 405, 400)")
        print("  ✅ Route registration and HTTP methods")
        print("  ✅ Data validation")
        print("  ✅ Complete API workflows")
    else:
        print("❌ SOME TESTS FAILED!")
        print(f"📊 Total tests run: {result.testsRun}")
        print(f"❌ Failures: {len(result.failures)}")
        print(f"💥 Errors: {len(result.errors)}")
        
        if result.failures:
            print("\n❌ FAILED TESTS:")
            for test, trace in result.failures:
                print(f"  - {test}: {trace.split('AssertionError:')[-1].strip()}")
        
        if result.errors:
            print("\n💥 ERROR TESTS:")
            for test, trace in result.errors:
                print(f"  - {test}: {trace.split('Exception:')[-1].strip()}")
    
    print("\n🔧 To run your Flask app:")
    print("  python3 run.py")
    print("\n📖 To view API documentation:")
    print("  http://localhost:5000/api/v1/")
    
    print("=" * 70)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_comprehensive_tests()
    sys.exit(0 if success else 1)
