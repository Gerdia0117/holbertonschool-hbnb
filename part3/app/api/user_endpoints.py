from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.business.facade import HBnBFacade
from app.utils.auth import admin_required, is_admin

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

# Model for admin user update - includes all fields
admin_user_update_model = api.model("AdminUserUpdate", {
    "first_name": fields.String(description="First name"),
    "last_name": fields.String(description="Last name"),
    "email": fields.String(description="Email address"),
    "password": fields.String(description="Password"),
    "is_admin": fields.Boolean(description="Admin status")
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

    @api.expect(admin_user_update_model)
    @api.marshal_with(user_model)
    @jwt_required()
    def put(self, user_id):
        """Update user details (requires authentication, admins can update any user)"""
        current_user_id = get_jwt_identity()
        admin = is_admin()
        
        # Check if user exists
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, "User not found")
        
        # Non-admin users can only update their own information
        if not admin and current_user_id != user_id:
            api.abort(403, "You can only update your own user information")
        
        update_data = api.payload.copy()
        
        # Regular users cannot update email, password, or admin status
        if not admin:
            update_data.pop('email', None)
            update_data.pop('password', None)
            update_data.pop('is_admin', None)
        
        # Update the user
        try:
            updated_user = facade.update_user(user_id, update_data)
            return updated_user
        except ValueError as e:
            api.abort(400, str(e))
