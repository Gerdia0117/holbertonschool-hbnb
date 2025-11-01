from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from app.business.facade import HBnBFacade
from app.utils.auth import admin_required

api = Namespace("amenities", description="Amenity operations")
facade = HBnBFacade()

amenity_model = api.model("Amenity", {
    "id": fields.String(readonly=True, description="Amenity ID"),
    "name": fields.String(required=True, description="Amenity name")
})


@api.route("/")
class AmenityList(Resource):
    @api.marshal_list_with(amenity_model)
    def get(self):
        return facade.get_all_amenities()

    @api.expect(amenity_model)
    @api.marshal_with(amenity_model, code=201)
    @jwt_required()
    @admin_required()
    def post(self):
        """Create a new amenity (admin only)"""
        try:
            return facade.create_amenity(api.payload), 201
        except ValueError as e:
            api.abort(400, str(e))


@api.route("/<string:amenity_id>")
@api.response(404, "Amenity not found")
class AmenityResource(Resource):
    @api.marshal_with(amenity_model)
    def get(self, amenity_id):
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api.abort(404, "Amenity not found")
        return amenity

    @api.expect(amenity_model)
    @api.marshal_with(amenity_model)
    @jwt_required()
    @admin_required()
    def put(self, amenity_id):
        """Update an amenity (admin only)"""
        amenity = facade.update_amenity(amenity_id, api.payload)
        if not amenity:
            api.abort(404, "Amenity not found")
        return amenity
