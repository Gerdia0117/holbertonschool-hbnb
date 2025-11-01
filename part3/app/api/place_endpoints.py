from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.business.facade import HBnBFacade
from app.utils.auth import is_admin

api = Namespace("places", description="Place operations")
facade = HBnBFacade()

place_model = api.model("Place", {
    "id": fields.String(readonly=True, description="Place ID"),
    "name": fields.String(required=True, description="Place name"),
    "description": fields.String(description="Place description"),
    "price": fields.Float(required=True, description="Price per night"),
    "latitude": fields.Float(description="Latitude coordinate"),
    "longitude": fields.Float(description="Longitude coordinate"),
    "owner_id": fields.String(description="Owner (User) ID"),
    "amenities": fields.List(fields.String, description="List of Amenity IDs")
})


@api.route("/")
class PlaceList(Resource):
    @api.marshal_list_with(place_model)
    def get(self):
        """List all places"""
        return facade.get_all_places()

    @api.expect(place_model)
    @api.marshal_with(place_model, code=201)
    @jwt_required()
    def post(self):
        """Create a new place (requires authentication)"""
        current_user_id = get_jwt_identity()
        place_data = api.payload
        # Set the owner_id to the authenticated user
        place_data['owner_id'] = current_user_id
        try:
            return facade.create_place(place_data), 201
        except ValueError as e:
            api.abort(400, str(e))


@api.route("/<string:place_id>")
@api.response(404, "Place not found")
class PlaceResource(Resource):
    @api.marshal_with(place_model)
    def get(self, place_id):
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, "Place not found")
        return place

    @api.expect(place_model)
    @api.marshal_with(place_model)
    @jwt_required()
    def put(self, place_id):
        """Update a place (requires authentication and ownership, or admin)"""
        current_user_id = get_jwt_identity()
        admin = is_admin()
        
        # Check if place exists
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, "Place not found")
        
        # Check ownership (admins can bypass)
        if not admin and not facade.is_place_owner(place_id, current_user_id):
            api.abort(403, "You do not have permission to update this place")
        
        # Update the place
        updated_place = facade.update_place(place_id, api.payload)
        return updated_place
