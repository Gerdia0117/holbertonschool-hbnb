from flask_restx import Namespace, Resource, fields
from app.business.facade import HBnBFacade

api = Namespace("users", description="User related operations")
facade = HBnBFacade()

user_model = api.model("User", {
    "id": fields.String(readonly=True, description="User ID"),
    "first_name": fields.String(required=True, description="First name"),
    "last_name": fields.String(required=True, description="Last name"),
    "email": fields.String(required=True, description="Email address")
})


@api.route("/")
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        return facade.get_all_users()

    @api.expect(user_model)
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
    def put(self, user_id):
        """Update an existing user"""
        user = facade.update_user(user_id, api.payload)
        if not user:
            api.abort(404, "User not found")
        return user
