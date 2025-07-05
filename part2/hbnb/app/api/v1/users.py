from flask_restx import Namespace, Resource, fields
from app.models.user import User
from app.services.facade import RentalServiceFacade

# Create namespace for users
api = Namespace('users', description='User operations')

# Define the user model for documentation
user_model = api.model('User', {
    'id': fields.String(required=True, description='User ID'),
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'email': fields.String(required=True, description='Email address'),
    'created_at': fields.DateTime(description='Creation date'),
    'updated_at': fields.DateTime(description='Last update date')
})

user_input_model = api.model('UserInput', {
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'email': fields.String(required=True, description='Email address'),
    'password': fields.String(required=True, description='Password')
})

# Initialize facade instance
facade = RentalServiceFacade()

@api.route('/')
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        """Get all users"""
        users = facade.get_all_users()
        return [user.to_dict() for user in users]

    @api.expect(user_input_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        data = api.payload
        
        # Input validation
        if not data.get('first_name') or not data.get('last_name'):
            api.abort(400, 'First name and last name are required')
        
        if not data.get('email'):
            api.abort(400, 'Email is required')
        
        if not data.get('password'):
            api.abort(400, 'Password is required')
        
        # Check if email already exists
        existing_user = facade.get_user_by_email(data['email'])
        if existing_user:
            api.abort(400, 'User with this email already exists')
        
        try:
            # Create new user through facade
            user = facade.create_user(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=data['password']
            )
            return user.to_dict(), 201
        except ValueError as e:
            api.abort(400, str(e))
        except Exception as e:
            api.abort(500, 'Internal server error')

@api.route('/<string:user_id>')
class UserResource(Resource):
    @api.marshal_with(user_model)
    def get(self, user_id):
        """Get a specific user"""
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, 'User not found')
        return user.to_dict()

    @api.expect(user_input_model)
    @api.marshal_with(user_model)
    def put(self, user_id):
        """Update a specific user"""
        data = api.payload
        
        # Check if user exists
        existing_user = facade.get_user(user_id)
        if not existing_user:
            api.abort(404, 'User not found')
        
        # Input validation
        if not data.get('first_name') or not data.get('last_name'):
            api.abort(400, 'First name and last name are required')
        
        if not data.get('email'):
            api.abort(400, 'Email is required')
        
        # Check if email is being changed and already exists
        if data['email'] != existing_user.email:
            user_with_email = facade.get_user_by_email(data['email'])
            if user_with_email:
                api.abort(400, 'User with this email already exists')
        
        try:
            # Update user through facade
            updated_user = facade.update_user(user_id, data)
            return updated_user.to_dict()
        except ValueError as e:
            api.abort(400, str(e))
        except Exception as e:
            api.abort(500, 'Internal server error')

    def delete(self, user_id):
        """Delete a specific user"""
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, 'User not found')
        
        try:
            facade.delete_user(user_id)
            return '', 204
        except Exception as e:
            api.abort(500, 'Internal server error')
