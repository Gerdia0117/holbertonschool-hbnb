#!/usr/bin/env python3
"""
Simple test file for HBnB Flask application using unittest
No additional dependencies required - works with standard Python library
"""

import unittest
import json
import sys
import os

# Add the current directory to the path to import the app
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import create_app


class TestHBnBApp(unittest.TestCase):
    """Test case for HBnB Flask application"""
    
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
        self.assertIsNotNone(self.app)
        self.assertEqual(self.app.name, 'app')
        self.assertIn('v1_api', self.app.blueprints)
        self.assertIn('restx_doc', self.app.blueprints)
    
    def test_swagger_ui_accessible(self):
        """Test that Swagger UI endpoint is accessible"""
        response = self.client.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.content_type)
        self.assertIn(b'HBnB Application API', response.data)
    
    def test_swagger_json_accessible(self):
        """Test that Swagger JSON spec is accessible"""
        response = self.client.get('/api/v1/swagger.json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        
        data = json.loads(response.data)
        self.assertIn('info', data)
        self.assertIn('paths', data)
        self.assertEqual(data['info']['title'], 'HBnB Application API')
    
    def test_users_endpoint_get(self):
        """Test GET request to users endpoint"""
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
    
    def test_users_endpoint_post_empty(self):
        """Test POST request to users endpoint with empty data"""
        response = self.client.post('/api/v1/users/',
                                  data=json.dumps({}),
                                  content_type='application/json')
        # Should return 400 or 422 for missing required fields
        self.assertIn(response.status_code, [400, 422])
    
    def test_users_endpoint_post_valid(self):
        """Test POST request to users endpoint with valid data"""
        user_data = {
            "first_name": "Test",
            "last_name": "User",
            "email": "test.user@example.com"
        }
        response = self.client.post('/api/v1/users/',
                                  data=json.dumps(user_data),
                                  content_type='application/json')
        # Should create user successfully (200 or 201)
        self.assertIn(response.status_code, [200, 201])
    
    def test_amenities_endpoint_get(self):
        """Test GET request to amenities endpoint"""
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
    
    def test_amenities_endpoint_post_empty(self):
        """Test POST request to amenities endpoint with empty data"""
        response = self.client.post('/api/v1/amenities/',
                                  data=json.dumps({}),
                                  content_type='application/json')
        # Should return 400 or 422 for missing required fields
        self.assertIn(response.status_code, [400, 422])
    
    def test_amenities_endpoint_post_valid(self):
        """Test POST request to amenities endpoint with valid data"""
        amenity_data = {
            "name": "Test Amenity"
        }
        response = self.client.post('/api/v1/amenities/',
                                  data=json.dumps(amenity_data),
                                  content_type='application/json')
        # Should create amenity successfully (200 or 201)
        self.assertIn(response.status_code, [200, 201])
    
    def test_user_not_found(self):
        """Test GET request for non-existent user"""
        response = self.client.get('/api/v1/users/non-existent-id')
        self.assertEqual(response.status_code, 404)
    
    def test_amenity_not_found(self):
        """Test GET request for non-existent amenity"""
        response = self.client.get('/api/v1/amenities/non-existent-id')
        self.assertEqual(response.status_code, 404)
    
    def test_invalid_endpoint(self):
        """Test request to non-existent endpoint"""
        response = self.client.get('/api/v1/invalid-endpoint')
        self.assertEqual(response.status_code, 404)
    
    def test_method_not_allowed(self):
        """Test wrong HTTP method on endpoint"""
        # Try DELETE on users list (should not be allowed)
        response = self.client.delete('/api/v1/users/')
        self.assertEqual(response.status_code, 405)
    
    def test_invalid_json(self):
        """Test request with invalid JSON data"""
        response = self.client.post('/api/v1/users/',
                                  data="invalid json",
                                  content_type='application/json')
        self.assertIn(response.status_code, [400, 422])
    
    def test_routes_registered(self):
        """Test that all expected routes are registered"""
        routes = [rule.rule for rule in self.app.url_map.iter_rules()]
        
        # Check main API routes
        self.assertIn('/api/v1/', routes)
        self.assertIn('/api/v1/users/', routes)
        self.assertIn('/api/v1/amenities/', routes)
        self.assertIn('/api/v1/swagger.json', routes)
        
        # Check that dynamic routes exist
        user_routes = [r for r in routes if '/api/v1/users/' in r and '<' in r]
        amenity_routes = [r for r in routes if '/api/v1/amenities/' in r and '<' in r]
        
        self.assertGreaterEqual(len(user_routes), 1)
        self.assertGreaterEqual(len(amenity_routes), 1)
    
    def test_route_methods(self):
        """Test that routes have correct HTTP methods"""
        rules = {rule.rule: rule.methods for rule in self.app.url_map.iter_rules()}
        
        # Test users endpoint methods
        users_methods = rules.get('/api/v1/users/')
        self.assertIn('GET', users_methods)
        self.assertIn('POST', users_methods)
        
        # Test amenities endpoint methods
        amenities_methods = rules.get('/api/v1/amenities/')
        self.assertIn('GET', amenities_methods)
        self.assertIn('POST', amenities_methods)


class TestAppIntegration(unittest.TestCase):
    """Integration tests for the application"""
    
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
    
    def test_complete_api_workflow(self):
        """Test a complete API workflow"""
        # Test documentation is accessible
        doc_response = self.client.get('/api/v1/')
        self.assertEqual(doc_response.status_code, 200)
        
        # Test API spec is accessible
        spec_response = self.client.get('/api/v1/swagger.json')
        self.assertEqual(spec_response.status_code, 200)
        
        # Test users endpoint
        users_response = self.client.get('/api/v1/users/')
        self.assertEqual(users_response.status_code, 200)
        
        # Test amenities endpoint
        amenities_response = self.client.get('/api/v1/amenities/')
        self.assertEqual(amenities_response.status_code, 200)
        
        print("✅ Complete API workflow test passed!")
    
    def test_api_consistency(self):
        """Test that API responses are consistent"""
        # All list endpoints should return JSON
        endpoints = ['/api/v1/users/', '/api/v1/amenities/']
        
        for endpoint in endpoints:
            response = self.client.get(endpoint)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')
        
        print("✅ API consistency test passed!")


def run_tests():
    """Run all tests and display results"""
    print("=" * 60)
    print("🧪 Running HBnB Flask Application Tests")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestHBnBApp))
    suite.addTests(loader.loadTestsFromTestCase(TestAppIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    if result.wasSuccessful():
        print("🎉 All tests passed successfully!")
        print(f"✅ Ran {result.testsRun} tests")
    else:
        print("❌ Some tests failed!")
        print(f"📊 Ran {result.testsRun} tests")
        print(f"❌ Failures: {len(result.failures)}")
        print(f"💥 Errors: {len(result.errors)}")
    
    print("=" * 60)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
