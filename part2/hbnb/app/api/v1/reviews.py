from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('feedbacks', description='Feedback operations')

feedback_model = api.model('Feedback', {
    'content': fields.String(required=True, description='Content of the feedback'),
    'score': fields.Integer(required=True, description='Score of the property (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'property_id': fields.String(required=True, description='ID of the property')
})


@api.route('/')
class FeedbackList(Resource):
    @api.expect(feedback_model)
    @api.response(201, 'Feedback successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Create a new feedback"""
        feedback_data = api.payload

        try:
            new_feedback = facade.create_feedback(feedback_data)
            return {
                'id': new_feedback.id,
                'content': new_feedback.comment,
                'score': new_feedback.score,
                'user_id': new_feedback.user.id,
                'property_id': new_feedback.property.id,
                'created_at': new_feedback.created_at.isoformat(),
                'updated_at': new_feedback.updated_at.isoformat()
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': 'An unexpected error occurred'}, 400

    @api.response(200, 'List of feedbacks retrieved successfully')
    def get(self):
        """Retrieve a list of all feedbacks"""
        try:
            feedbacks = facade.get_all_feedbacks()
            return [
                {
                    'id': feedback.id,
                    'content': feedback.comment,
                    'score': feedback.score,
                    'user_id': feedback.user.id,
                    'property_id': feedback.property.id,
                    'created_at': feedback.created_at.isoformat(),
                    'updated_at': feedback.updated_at.isoformat()
                } for feedback in feedbacks
            ], 200
        except Exception as e:
            return {'error': str(e)}, 500


@api.route('/<feedback_id>')
class FeedbackResource(Resource):
    @api.response(200, 'Feedback details retrieved successfully')
    @api.response(404, 'Feedback not found')
    def get(self, feedback_id):
        """Get feedback details by ID"""
        try:
            feedback = facade.get_feedback(feedback_id)
            if not feedback:
                return {'error': 'Feedback not found'}, 404
            return {
                'id': feedback.id,
                'content': feedback.comment,
                'score': feedback.score,
                'user_id': feedback.user.id,
                'property_id': feedback.property.id,
                'created_at': feedback.created_at.isoformat(),
                'updated_at': feedback.updated_at.isoformat()
            }, 200
        except Exception as e:
            return {'error': str(e)}, 500

    @api.expect(feedback_model)
    @api.response(200, 'Feedback updated successfully')
    @api.response(404, 'Feedback not found')
    @api.response(400, 'Invalid input data')
    def put(self, feedback_id):
        """Update feedback's information"""
        feedback_data = api.payload

        try:
            updated_feedback = facade.update_feedback(feedback_id, feedback_data)
            if not updated_feedback:
                return {'error': 'Feedback not found'}, 404

            return {
                'id': updated_feedback.id,
                'content': updated_feedback.comment,
                'score': updated_feedback.score,
                'user_id': updated_feedback.user.id,
                'property_id': updated_feedback.property.id,
                'created_at': updated_feedback.created_at.isoformat(),
                'updated_at': updated_feedback.updated_at.isoformat()
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': 'An unexpected error occurred'}, 400

    @api.response(200, 'Feedback deleted successfully')
    @api.response(404, 'Feedback not found')
    def delete(self, feedback_id):
        """Delete a feedback"""
        pass


@api.route('/properties/<property_id>/feedbacks')
class PropertyFeedbackList(Resource):
    @api.response(200, 'List of feedbacks for the property retrieved successfully')
    @api.response(404, 'Property not found')
    def get(self, property_id):
        """Get all feedbacks for a specific property"""
        try:
            property_feedbacks = facade.get_feedbacks_by_property(property_id)
            return [
                {
                    'id': feedback.id,
                    'content': feedback.comment,
                    'score': feedback.score,
                    'user_id': feedback.user.id,
                    'property_id': feedback.property.id,
                    'created_at': feedback.created_at.isoformat(),
                    'updated_at': feedback.updated_at.isoformat()
                } for feedback in property_feedbacks
            ], 200
        except Exception as e:
            return {'error': str(e)}, 500
from flask_restx import Namespace, Resource, fields
from app.services import facade

# Define the API namespace for 'feedbacks'
api = Namespace('feedbacks', description='Feedback operations')

# Define the feedback model for input validation and documentation
feedback_model = api.model('Feedback', {
    'content': fields.String(required=True, description='Content of the feedback'),
    'score': fields.Integer(required=True, description='Score of the property (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'property_id': fields.String(required=True, description='ID of the property')
})


@api.route('/')
class FeedbackList(Resource):
    @api.expect(feedback_model)
    @api.response(201, 'Feedback successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Create a new feedback"""
        feedback_data = api.payload

        try:
            # Create a new feedback using the facade
            new_feedback = facade.create_feedback(feedback_data)
            return {
                'id': new_feedback.id,
                'content': new_feedback.comment,
                'score': new_feedback.score,
                'user_id': new_feedback.user.id,
                'property_id': new_feedback.property.id,
                'created_at': new_feedback.created_at.isoformat(),
                'updated_at': new_feedback.updated_at.isoformat()
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': 'An unexpected error occurred'}, 400

    @api.response(200, 'List of feedbacks retrieved successfully')
    def get(self):
        """Retrieve a list of all feedbacks"""
        try:
            feedbacks = facade.get_all_feedbacks()
            return [
                {
                    'id': feedback.id,
                    'content': feedback.comment,
                    'score': feedback.score,
                    'user_id': feedback.user.id,
                    'property_id': feedback.property.id,
                    'created_at': feedback.created_at.isoformat(),
                    'updated_at': feedback.updated_at.isoformat()
                } for feedback in feedbacks
            ], 200
        except Exception as e:
            return {'error': str(e)}, 500


@api.route('/<feedback_id>')
class FeedbackResource(Resource):
    @api.response(200, 'Feedback details retrieved successfully')
    @api.response(404, 'Feedback not found')
    def get(self, feedback_id):
        """Get feedback details by ID"""
        try:
            feedback = facade.get_feedback(feedback_id)
            if not feedback:
                return {'error': 'Feedback not found'}, 404
            return {
                'id': feedback.id,
                'content': feedback.comment,
                'score': feedback.score,
                'user_id': feedback.user.id,
                'property_id': feedback.property.id,
                'created_at': feedback.created_at.isoformat(),
                'updated_at': feedback.updated_at.isoformat()
            }, 200
        except Exception as e:
            return {'error': str(e)}, 500

    @api.expect(feedback_model)
    @api.response(200, 'Feedback updated successfully')
    @api.response(404, 'Feedback not found')
    @api.response(400, 'Invalid input data')
    def put(self, feedback_id):
        """Update feedback's information"""
        feedback_data = api.payload

        try:
            updated_feedback = facade.update_feedback(feedback_id, feedback_data)
            if not updated_feedback:
                return {'error': 'Feedback not found'}, 404

            return {
                'id': updated_feedback.id,
                'content': updated_feedback.comment,
                'score': updated_feedback.score,
                'user_id': updated_feedback.user.id,
                'property_id': updated_feedback.property.id,
                'created_at': updated_feedback.created_at.isoformat(),
                'updated_at': updated_feedback.updated_at.isoformat()
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': 'An unexpected error occurred'}, 400

    @api.response(200, 'Feedback deleted successfully')
    @api.response(404, 'Feedback not found')
    def delete(self, feedback_id):
        """Delete a feedback"""
        # Placeholder for the logic to delete a feedback
        pass


@api.route('/properties/<property_id>/feedbacks')
class PropertyFeedbackList(Resource):
    @api.response(200, 'List of feedbacks for the property retrieved successfully')
    @api.response(404, 'Property not found')
    def get(self, property_id):
        """Get all feedbacks for a specific property"""
        try:
            property_feedbacks = facade.get_feedbacks_by_property(property_id)
            return [
                {
                    'id': feedback.id,
                    'content': feedback.comment,
                    'score': feedback.score,
                    'user_id': feedback.user.id,
                    'property_id': feedback.property.id,
                    'created_at': feedback.created_at.isoformat(),
                    'updated_at': feedback.updated_at.isoformat()
                } for feedback in property_feedbacks
            ], 200
        except Exception as e:
            return {'error': str(e)}, 500
