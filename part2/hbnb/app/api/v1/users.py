from flask_restx import Namespace, Resource, fields
from app.models.user import User

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

@api.route('/')
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        """Get all users"""
        # This will eventually get users from your data storage
        return []

    @api.expect(user_input_model)
    @api.marshal_with(user_model)
    def post(self):
        """Create a new user"""
        data = api.payload
        user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password']
        )
        # Here you would save the user to your data storage
        return user.__dict__, 201

@api.route('/<string:user_id>')
class UserResource(Resource):
    @api.marshal_with(user_model)
    def get(self, user_id):
        """Get a specific user"""
        # This will eventually get user from your data storage
        user = User(first_name="John", last_name="Doe", email="john@example.com")
        user.id = user_id
        return user.__dict__

    @api.expect(user_input_model)
    @api.marshal_with(user_model)
    def put(self, user_id):
        """Update a specific user"""
        data = api.payload
        # Here you would update the user in your data storage
        user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password']
        )
        user.id = user_id
        return user.__dict__

    def delete(self, user_id):
        """Delete a specific user"""
        # Here you would delete the user from your data storage
        return '', 204
