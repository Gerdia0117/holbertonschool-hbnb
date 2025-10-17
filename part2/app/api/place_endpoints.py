from flask_restx import Namespace, Resource, fields
from app.business.facade import HBnBFacade

api = Namespace("places", description="Place operations")
facade = HBnBFacade()

# Model schema for docs + validation
place_model = api.model("Place", {
    "id": fields.String(readonly=True, description="Place ID"),
    "name": fields.String(required=True, description="Place name"),
    "description": fields.String(description="Place description"),
    "price": fields.Float(required=True, description="Price per night"),
    "latitude": fields.Float(description="Latitude coordinate"),
    "longitude": fields.Float(description="Longitude coordinate"),
    "owner_id": fields.String(description="Owner (User) ID"),
    "amenities": fields.List(fields.String, description="List of Amenity IDs"),
    "reviews": fields.List(fields.String, description="List of Review IDs")
})

@api.route("/")
class PlaceList(Resource):
    @api.marshal_list_with(place_model)
    def get(self):
        """List all places with related amenities and reviews."""
        places = facade.get_all_places()
        for place in places:
            # Attach amenities IDs if they exist
            place.amenities = [a.id for a in getattr(place, "amenities", [])]
            # Attach review IDs for the place
            place.reviews = [r.id for r in facade.get_reviews_by_place(place.id)]
        return places

    @api.expect(place_model)
    @api.marshal_with(place_model, code=201)
    def post(self):
        """Create a new place."""
        try:
            place = facade.create_place(api.payload)
            place.amenities = []  # initialize empty amenities list
            place.reviews = []    # initialize empty reviews list
            return place, 201
        except ValueError as e:
            api.abort(400, str(e))


@api.route("/<string:place_id>")
@api.response(404, "Place not found")
class PlaceResource(Resource):
    @api.marshal_with(place_model)
    def get(self, place_id):
        """Retrieve a single place with amenities and reviews."""
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, "Place not found")

        # Attach amenities and reviews
        place.amenities = [a.id for a in getattr(place, "amenities", [])]
        place.reviews = [r.id for r in facade.get_reviews_by_place(place.id)]
        return place

    @api.expect(place_model)
    @api.marshal_with(place_model)
    def put(self, place_id):
        """Update an existing place."""
        place = facade.update_place(place_id, api.payload)
        if not place:
            api.abort(404, "Place not found")

        # Update amenities and reviews for response
        place.amenities = [a.id for a in getattr(place, "amenities", [])]
        place.reviews = [r.id for r in facade.get_reviews_by_place(place.id)]
        return place
