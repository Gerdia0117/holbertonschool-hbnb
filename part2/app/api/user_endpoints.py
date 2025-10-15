from flask import request
from flask_restx import Namespace, Resource, fields
from app.models.user import User
from app.services.storage_service import storage

api = Namespace("users", description="User operations")

user_model = api.model("User", {
    "id": fields.String(readonly=True, description="User ID"),
    "first_name": fields.String(required=True),
    "last_name": fields.String,
    "email": fields.String(required=True),
})

@api.route("/")
class UserList(Resource):
    """Handles creation and retrieval of all users"""

    @api.marshal_list_with(user_model)
    def get(self):
        """Retrieve all users"""
        users = storage.get_all_users()
        return [u.to_dict() for u in users], 200

    @api.expect(user_model, validate=True)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        data = request.json
        new_user = User(**data)
        storage.add_user(new_user)
        return new_user.to_dict(), 201


@api.route("/<string:user_id>")
@api.param("user_id", "The user identifier")
class UserResource(Resource):
    """Handles operations on a single user"""

    @api.marshal_with(user_model)
    def get(self, user_id):
        """Retrieve user by ID"""
        user = storage.get_user(user_id)
        if not user:
            api.abort(404, "User not found")
        return user.to_dict()

    @api.expect(user_model)
    @api.marshal_with(user_model)
    def put(self, user_id):
        """Update a user's information"""
        user = storage.update_user(user_id, request.json)
        if not user:
            api.abort(404, "User not found")
        return user.to_dict(), 200
