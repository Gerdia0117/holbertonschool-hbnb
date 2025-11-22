"""
Authentication endpoints for JWT-based login.
"""
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.business.facade import HBnBFacade

api = Namespace("auth", description="Authentication operations")
facade = HBnBFacade()

# Model for login input
login_model = api.model("Login", {
    "email": fields.String(required=True, description="User email"),
    "password": fields.String(required=True, description="User password")
})

# Model for login response
token_model = api.model("Token", {
    "access_token": fields.String(description="JWT access token")
})


@api.route("/login")
class Login(Resource):
    @api.expect(login_model)
    @api.response(200, "Login successful", token_model)
    @api.response(401, "Invalid credentials")
    def post(self):
        """
        Authenticate user and return a JWT token.
        
        The token includes user identity and claims (like is_admin).
        """
        credentials = api.payload
        email = credentials.get("email")
        password = credentials.get("password")
        
        if not email or not password:
            api.abort(400, "Email and password are required")
        
        # Get user by email
        user = facade.get_user_by_email(email)
        
        if not user or not user.verify_password(password):
            api.abort(401, "Invalid credentials")
        
        # Create JWT token with additional claims
        access_token = create_access_token(
            identity=user.id,
            additional_claims={
                "is_admin": user.is_admin
            }
        )
        
        return {"access_token": access_token}, 200
