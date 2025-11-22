"""
Protected endpoints that require JWT authentication.
"""
from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

api = Namespace("protected", description="Protected operations requiring JWT")


@api.route("/test")
class ProtectedTest(Resource):
    @jwt_required()
    def get(self):
        """
        A protected endpoint that requires a valid JWT token.
        
        Use this to test JWT authentication.
        """
        current_user_id = get_jwt_identity()
        jwt_data = get_jwt()
        
        return {
            "message": "This is a protected endpoint",
            "user_id": current_user_id,
            "is_admin": jwt_data.get("is_admin", False)
        }, 200


@api.route("/admin-only")
class AdminOnly(Resource):
    @jwt_required()
    def get(self):
        """
        A protected endpoint that only admin users should access.
        
        Demonstrates using JWT claims for authorization.
        """
        jwt_data = get_jwt()
        is_admin = jwt_data.get("is_admin", False)
        
        if not is_admin:
            api.abort(403, "Admin access required")
        
        return {
            "message": "Welcome, admin!",
            "user_id": get_jwt_identity()
        }, 200
