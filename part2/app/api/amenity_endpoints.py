from flask_restx import Namespace, Resource, fields
from app.business.facade import HBnBFacade

api = Namespace("amenities", description="Amenity operations")

# Amenity model for documentation and validation
amenity_model = api.model("Amenity", {
    "id": fields.String(readonly=True, description="Amenity ID"),
    "name": fields.String(required=True, description="Amenity name")
})

facade = HBnBFacade()

@api.route("/")
class AmenityList(Resource):
    @api.marshal_list_with(amenity_model)
    def get(self):
        """Retrieve all amenities"""
        return facade.get_all_amenities()

    @api.expect(amenity_model)
    @api.marshal_with(amenity_model, code=201)
    def post(self):
        """Create a new amenity"""
        return facade.create_amenity(api.payload), 201


@api.route("/<string:amenity_id>")
@api.response(404, "Amenity not found")
class AmenityResource(Resource):
    @api.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Retrieve an amenity by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api.abort(404, "Amenity not found")
        return amenity

    @api.expect(amenity_model)
    @api.marshal_with(amenity_model)
    def put(self, amenity_id):
        """Update an existing amenity"""
        amenity = facade.update_amenity(amenity_id, api.payload)
        if not amenity:
            api.abort(404, "Amenity not found")
        return amenity
