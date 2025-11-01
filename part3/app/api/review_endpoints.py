from flask_restx import Namespace, Resource, fields
from app.business.facade import HBnBFacade

api = Namespace("reviews", description="Review operations")
facade = HBnBFacade()

review_model = api.model("Review", {
    "id": fields.String(readonly=True, description="Review ID"),
    "text": fields.String(required=True, description="Review text"),
    "user_id": fields.String(required=True, description="Author User ID"),
    "place_id": fields.String(required=True, description="Associated Place ID")
})


@api.route("/")
class ReviewList(Resource):
    @api.marshal_list_with(review_model)
    def get(self):
        return facade.get_all_reviews()

    @api.expect(review_model)
    @api.marshal_with(review_model, code=201)
    def post(self):
        try:
            return facade.create_review(api.payload), 201
        except ValueError as e:
            api.abort(400, str(e))


@api.route("/<string:review_id>")
@api.response(404, "Review not found")
class ReviewResource(Resource):
    @api.marshal_with(review_model)
    def get(self, review_id):
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Review not found")
        return review

    @api.expect(review_model)
    @api.marshal_with(review_model)
    def put(self, review_id):
        review = facade.update_review(review_id, api.payload)
        if not review:
            api.abort(404, "Review not found")
        return review

    def delete(self, review_id):
        success = facade.delete_review(review_id)
        if not success:
            api.abort(404, "Review not found")
        return {"message": "Review deleted"}, 200


@api.route("/place/<string:place_id>")
class ReviewsByPlace(Resource):
    @api.marshal_list_with(review_model)
    def get(self, place_id):
        return facade.get_reviews_by_place(place_id)
