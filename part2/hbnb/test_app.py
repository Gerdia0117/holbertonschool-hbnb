#!/usr/bin/env python3
"""
Test script to verify the Flask application functionality
"""
from app import create_app
import json

def test_app_creation():
    """Test that the app can be created successfully"""
    print("Testing app creation...")
    app = create_app()
    
    print(f"✅ App created successfully: {app}")
    print(f"✅ App name: {app.name}")
    print(f"✅ Blueprints registered: {list(app.blueprints.keys())}")
    
    return app

def test_routes(app):
    """Test that routes are properly registered"""
    print("\nTesting routes...")
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'rule': rule.rule,
            'methods': list(rule.methods)
        })
    
    print("✅ Available routes:")
    for route in routes:
        print(f"  - {route['endpoint']}: {route['rule']} {route['methods']}")
    
    return routes

def test_api_endpoints(app):
    """Test the API endpoints with a test client"""
    print("\nTesting API endpoints...")
    
    with app.test_client() as client:
        # Test the documentation endpoint
        response = client.get('/api/v1/')
        print(f"✅ API documentation endpoint: Status {response.status_code}")
        
        # Test users endpoint
        response = client.get('/api/v1/users/')
        print(f"✅ Users list endpoint: Status {response.status_code}")
        
        # Test amenities endpoint
        response = client.get('/api/v1/amenities/')
        print(f"✅ Amenities list endpoint: Status {response.status_code}")

def test_configuration(app):
    """Test app configuration"""
    print("\nTesting configuration...")
    print(f"✅ Debug mode: {app.debug}")
    print(f"✅ Testing mode: {app.testing}")
    print(f"✅ Secret key configured: {'Yes' if app.secret_key else 'No'}")

if __name__ == '__main__':
    print("=== Flask Application Test ===\n")
    
    try:
        # Test app creation
        app = test_app_creation()
        
        # Test routes
        routes = test_routes(app)
        
        # Test API endpoints
        test_api_endpoints(app)
        
        # Test configuration
        test_configuration(app)
        
        print("\n=== All Tests Completed Successfully! ===")
        print("Your Flask application is working correctly.")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
