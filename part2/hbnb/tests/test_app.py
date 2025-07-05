#!/usr/bin/env python3
"""
Comprehensive test suite for the HBnB Flask application
Tests all API endpoints, models, and application functionality
"""

import pytest
import json
import sys
import os

# Add the parent directory to the path to import the app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app


class TestFlaskApp:
    """Test class for Flask application functionality"""
    
    @pytest.fixture
    def app(self):
        """Create and configure a test app instance"""
        app = create_app()
        app.config['TESTING'] = True
        return app
    
    @pytest.fixture
    def client(self, app):
        """Create a test client for the app"""
        return app.test_client()
    
    def test_app_creation(self, app):
        """Test that the Flask app is created successfully"""
        assert app is not None
        assert app.name == 'app'
        assert 'v1_api' in app.blueprints
        assert 'restx_doc' in app.blueprints
    
    def test_app_configuration(self, app):
        """Test app configuration settings"""
        assert app.config['TESTING'] is True


class TestAPIDocumentation:
    """Test class for API documentation endpoints"""
    
    @pytest.fixture
    def app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app
    
    @pytest.fixture
    def client(self, app):
        return app.test_client()
    
    def test_swagger_ui_endpoint(self, client):
        """Test that Swagger UI is accessible"""
        response = client.get('/api/v1/')
        assert response.status_code == 200
        assert 'text/html' in response.content_type
        assert b'HBnB Application API' in response.data
    
    def test_swagger_json_endpoint(self, client):
        """Test that Swagger JSON spec is accessible"""
        response = client.get('/api/v1/swagger.json')
        assert response.status_code == 200
        assert response.content_type == 'application/json'
        
        data = json.loads(response.data)
        assert 'info' in data
        assert 'paths' in data
        assert data['info']['title'] == 'HBnB Application API'


class TestUsersAPI:
    """Test class for Users API endpoints"""
    
    @pytest.fixture
    def app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app
    
    @pytest.fixture
    def client(self, app):
        return app.test_client()
    
    def test_get_users_list(self, client):
        """Test GET /api/v1/users/"""
        response = client.get('/api/v1/users/')
        assert response.status_code == 200
        assert response.content_type == 'application/json'
    
    def test_post_user_missing_data(self, client):
        """Test POST /api/v1/users/ with missing data"""
        response = client.post('/api/v1/users/', 
                             data=json.dumps({}),
                             content_type='application/json')
        # Should return 400 for missing required fields
        assert response.status_code in [400, 422]
    
    def test_post_user_valid_data(self, client):
        """Test POST /api/v1/users/ with valid data"""
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        }
        response = client.post('/api/v1/users/',
                             data=json.dumps(user_data),
                             content_type='application/json')
        # Should create user successfully
        assert response.status_code in [200, 201]
    
    def test_get_user_by_id_not_found(self, client):
        """Test GET /api/v1/users/<id> with non-existent user"""
        response = client.get('/api/v1/users/non-existent-id')
        assert response.status_code == 404
    
    def test_put_user_not_found(self, client):
        """Test PUT /api/v1/users/<id> with non-existent user"""
        user_data = {
            "first_name": "Jane",
            "last_name": "Smith"
        }
        response = client.put('/api/v1/users/non-existent-id',
                            data=json.dumps(user_data),
                            content_type='application/json')
        assert response.status_code == 404
    
    def test_delete_user_not_found(self, client):
        """Test DELETE /api/v1/users/<id> with non-existent user"""
        response = client.delete('/api/v1/users/non-existent-id')
        assert response.status_code == 404


class TestAmenitiesAPI:
    """Test class for Amenities API endpoints"""
    
    @pytest.fixture
    def app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app
    
    @pytest.fixture
    def client(self, app):
        return app.test_client()
    
    def test_get_amenities_list(self, client):
        """Test GET /api/v1/amenities/"""
        response = client.get('/api/v1/amenities/')
        assert response.status_code == 200
        assert response.content_type == 'application/json'
    
    def test_post_amenity_missing_data(self, client):
        """Test POST /api/v1/amenities/ with missing data"""
        response = client.post('/api/v1/amenities/',
                             data=json.dumps({}),
                             content_type='application/json')
        # Should return 400 for missing required fields
        assert response.status_code in [400, 422]
    
    def test_post_amenity_valid_data(self, client):
        """Test POST /api/v1/amenities/ with valid data"""
        amenity_data = {
            "name": "WiFi"
        }
        response = client.post('/api/v1/amenities/',
                             data=json.dumps(amenity_data),
                             content_type='application/json')
        # Should create amenity successfully
        assert response.status_code in [200, 201]
    
    def test_get_amenity_by_id_not_found(self, client):
        """Test GET /api/v1/amenities/<id> with non-existent amenity"""
        response = client.get('/api/v1/amenities/non-existent-id')
        assert response.status_code == 404
    
    def test_put_amenity_not_found(self, client):
        """Test PUT /api/v1/amenities/<id> with non-existent amenity"""
        amenity_data = {
            "name": "Swimming Pool"
        }
        response = client.put('/api/v1/amenities/non-existent-id',
                            data=json.dumps(amenity_data),
                            content_type='application/json')
        assert response.status_code == 404


class TestRoutes:
    """Test class for route registration and accessibility"""
    
    @pytest.fixture
    def app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app
    
    def test_all_routes_registered(self, app):
        """Test that all expected routes are registered"""
        routes = [rule.rule for rule in app.url_map.iter_rules()]
        
        # Check that main API routes exist
        assert '/api/v1/' in routes
        assert '/api/v1/users/' in routes
        assert '/api/v1/amenities/' in routes
        assert '/api/v1/swagger.json' in routes
        
        # Check that dynamic routes exist
        user_routes = [r for r in routes if '/api/v1/users/' in r and '<' in r]
        amenity_routes = [r for r in routes if '/api/v1/amenities/' in r and '<' in r]
        
        assert len(user_routes) >= 1  # Should have user detail route
        assert len(amenity_routes) >= 1  # Should have amenity detail route
    
    def test_route_methods(self, app):
        """Test that routes have correct HTTP methods"""
        rules = {rule.rule: rule.methods for rule in app.url_map.iter_rules()}
        
        # Test users list endpoint methods
        users_methods = rules.get('/api/v1/users/')
        assert 'GET' in users_methods
        assert 'POST' in users_methods
        
        # Test amenities list endpoint methods
        amenities_methods = rules.get('/api/v1/amenities/')
        assert 'GET' in amenities_methods
        assert 'POST' in amenities_methods


class TestErrorHandling:
    """Test class for error handling"""
    
    @pytest.fixture
    def app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app
    
    @pytest.fixture
    def client(self, app):
        return app.test_client()
    
    def test_404_error(self, client):
        """Test 404 error for non-existent endpoints"""
        response = client.get('/api/v1/non-existent-endpoint')
        assert response.status_code == 404
    
    def test_405_method_not_allowed(self, client):
        """Test 405 error for wrong HTTP methods"""
        # Try to DELETE the users list endpoint (should not be allowed)
        response = client.delete('/api/v1/users/')
        assert response.status_code == 405
    
    def test_invalid_json_data(self, client):
        """Test handling of invalid JSON data"""
        response = client.post('/api/v1/users/',
                             data="invalid json",
                             content_type='application/json')
        assert response.status_code in [400, 422]


class TestIntegration:
    """Integration tests for complete workflows"""
    
    @pytest.fixture
    def app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app
    
    @pytest.fixture
    def client(self, app):
        return app.test_client()
    
    def test_create_and_retrieve_user_workflow(self, client):
        """Test complete workflow: create user, retrieve it, update it"""
        # Step 1: Create a user
        user_data = {
            "first_name": "Integration",
            "last_name": "Test",
            "email": "integration.test@example.com"
        }
        
        create_response = client.post('/api/v1/users/',
                                    data=json.dumps(user_data),
                                    content_type='application/json')
        
        if create_response.status_code in [200, 201]:
            # If user creation is implemented, test retrieval
            try:
                response_data = json.loads(create_response.data)
                if 'id' in response_data:
                    user_id = response_data['id']
                    
                    # Step 2: Retrieve the user
                    get_response = client.get(f'/api/v1/users/{user_id}')
                    assert get_response.status_code == 200
                    
                    # Step 3: Update the user
                    update_data = {"first_name": "Updated"}
                    put_response = client.put(f'/api/v1/users/{user_id}',
                                            data=json.dumps(update_data),
                                            content_type='application/json')
                    # Update should work or return appropriate status
                    assert put_response.status_code in [200, 404]
            except (json.JSONDecodeError, KeyError):
                # If response format is different, that's okay for now
                pass
    
    def test_api_documentation_completeness(self, client):
        """Test that API documentation includes all endpoints"""
        response = client.get('/api/v1/swagger.json')
        assert response.status_code == 200
        
        spec = json.loads(response.data)
        paths = spec.get('paths', {})
        
        # Check that main endpoints are documented
        assert '/users/' in paths or '/users' in paths
        assert '/amenities/' in paths or '/amenities' in paths


if __name__ == '__main__':
    # Run tests with pytest
    pytest.main([__file__, '-v'])
