from flask_restx import Namespace, Resource, fields
from app.business.facade import HBnBFacade

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
    def post(self):
        """Create a new place"""
        try:
            return facade.create_place(api.payload), 201
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
    def put(self, place_id):
        place = facade.update_place(place_id, api.payload)
        if not place:
            api.abort(404, "Place not found")
        return place
