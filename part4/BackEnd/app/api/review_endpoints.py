from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.business.facade import HBnBFacade
from app.utils.auth import is_admin

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
    @jwt_required()
    def post(self):
        """Create a new review (requires authentication)"""
        current_user_id = get_jwt_identity()
        review_data = api.payload
        # Set the user_id to the authenticated user
        review_data['user_id'] = current_user_id
        try:
            return facade.create_review(review_data), 201
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
    @jwt_required()
    def put(self, review_id):
        """Update a review (requires authentication and ownership, or admin)"""
        current_user_id = get_jwt_identity()
        admin = is_admin()
        
        # Check if review exists
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Review not found")
        
        # Check ownership (admins can bypass)
        if not admin and not facade.is_review_author(review_id, current_user_id):
            api.abort(403, "You do not have permission to update this review")
        
        # Update the review
        updated_review = facade.update_review(review_id, api.payload)
        return updated_review

    @jwt_required()
    def delete(self, review_id):
        """Delete a review (requires authentication and ownership, or admin)"""
        current_user_id = get_jwt_identity()
        admin = is_admin()
        
        # Check if review exists
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Review not found")
        
        # Check ownership (admins can bypass)
        if not admin and not facade.is_review_author(review_id, current_user_id):
            api.abort(403, "You do not have permission to delete this review")
        
        # Delete the review
        success = facade.delete_review(review_id)
        if not success:
            api.abort(404, "Review not found")
        return {"message": "Review deleted"}, 200


@api.route("/place/<string:place_id>")
class ReviewsByPlace(Resource):
    @api.marshal_list_with(review_model)
    def get(self, place_id):
        return facade.get_reviews_by_place(place_id)
