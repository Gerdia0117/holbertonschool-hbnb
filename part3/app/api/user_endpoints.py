from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.business.facade import HBnBFacade

api = Namespace("users", description="User related operations")
facade = HBnBFacade()

# Model for output (GET requests) - no password
user_model = api.model("User", {
    "id": fields.String(readonly=True, description="User ID"),
    "first_name": fields.String(required=True, description="First name"),
    "last_name": fields.String(required=True, description="Last name"),
    "email": fields.String(required=True, description="Email address")
})

# Model for input (POST requests) - includes password
user_input_model = api.model("UserInput", {
    "first_name": fields.String(required=True, description="First name"),
    "last_name": fields.String(required=True, description="Last name"),
    "email": fields.String(required=True, description="Email address"),
    "password": fields.String(required=True, description="Password")
})


@api.route("/")
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        return facade.get_all_users()

    @api.expect(user_input_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        try:
            return facade.create_user(api.payload), 201
        except ValueError as e:
            api.abort(400, str(e))


@api.route("/<string:user_id>")
@api.response(404, "User not found")
class UserResource(Resource):
    @api.marshal_with(user_model)
    def get(self, user_id):
        """Retrieve a single user by ID"""
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, "User not found")
        return user

    @api.expect(user_model)
    @api.marshal_with(user_model)
    @jwt_required()
    def put(self, user_id):
        """Update user details (requires authentication)"""
        current_user_id = get_jwt_identity()
        
        # Users can only update their own information
        if current_user_id != user_id:
            api.abort(403, "You can only update your own user information")
        
        # Check if user exists
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, "User not found")
        
        # Prevent updating email and password through this endpoint
        update_data = api.payload.copy()
        update_data.pop('email', None)
        update_data.pop('password', None)
        
        # Update the user
        updated_user = facade.update_user(user_id, update_data)
        return updated_user
