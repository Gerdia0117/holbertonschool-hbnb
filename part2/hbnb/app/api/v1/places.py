from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('properties', description='Property management operations')

facility_model = api.model('PropertyFacility', {
    'id': fields.String(description='Facility ID'),
    'name': fields.String(description='Name of the facility')
})

owner_model = api.model('PropertyOwner', {
    'id': fields.String(description='Owner ID'),
    'first_name': fields.String(description='First name of the property owner'),
    'last_name': fields.String(description='Last name of the property owner'),
    'email': fields.String(description='Email of the property owner')
})

property_model = api.model('Property', {
    'name': fields.String(required=True, description='Name of the property'),
    'description': fields.String(description='Description of the property'),
    'price_per_night': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the property'),
    'longitude': fields.Float(required=True, description='Longitude of the property'),
    'owner_id': fields.String(required=True, description='ID of the property owner'),
    'facilities': fields.List(fields.String, required=True, description="List of facility IDs")
})


@api.route('/')
class PropertyList(Resource):
    @api.expect(property_model)
    @api.response(201, 'Property successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Add a new property"""
        property_data = api.payload

        try:
            required_fields = ['name', 'price_per_night', 'latitude', 'longitude', 'owner_id']
            for field in required_fields:
                if field not in property_data or property_data[field] is None:
                    return {'error': f'Missing required field: {field}'}, 400

            if (not isinstance(property_data['price_per_night'], (int, float)) or property_data['price_per_night'] <= 0):
                return {'error': 'Price must be a positive number'}, 400

            if (not isinstance(property_data['latitude'], (int, float)) or not (-90 <= property_data['latitude'] <= 90)):
                return {'error': 'Latitude must be between -90 and 90'}, 400

            if (not isinstance(property_data['longitude'], (int, float)) or not (-180 <= property_data['longitude'] <= 180)):
                return {'error': 'Longitude must be between -180 and 180'}, 400

            new_property = facade.add_property(property_data)

            return {
                'id': new_property.id,
                'name': new_property.name,
                'description': new_property.description,
                'price_per_night': new_property.price_per_night,
                'latitude': new_property.latitude,
                'longitude': new_property.longitude,
                'owner_id': new_property.owner.id,
                'facilities': [facility.id for facility in new_property.facilities],
                'created_at': new_property.created_at.isoformat(),
                'updated_at': new_property.updated_at.isoformat()
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': str(e)}, 500

    @api.response(200, 'List of properties retrieved successfully')
    def get(self):
        """Retrieve a list of all properties"""
        try:
            properties = facade.get_all_properties()
            return [
                {
                    'id': property.id,
                    'name': property.name,
                    'price_per_night': property.price_per_night,
                    'latitude': property.latitude,
                    'longitude': property.longitude,
                    'owner_id': property.owner.id,
                    'facilities': [facility.id for facility in property.facilities],
                    'created_at': property.created_at.isoformat(),
                    'updated_at': property.updated_at.isoformat()
                }
                for property in properties
            ], 200
        except Exception as e:
            return {'error': str(e)}, 500


@api.route('/<property_id>')
class PropertyResource(Resource):
    @api.response(200, 'Property details retrieved successfully')
    @api.response(404, 'Property not found')
    def get(self, property_id):
        """Get property details by ID"""
        try:
            property = facade.get_property(property_id)
            if not property:
                return {'error': 'Property not found'}, 404
            return {
                'id': property.id,
                'name': property.name,
                'description': property.description,
                'price_per_night': property.price_per_night,
                'latitude': property.latitude,
                'longitude': property.longitude,
                'owner': {
                    'id': property.owner.id,
                    'first_name': property.owner.first_name,
                    'last_name': property.owner.last_name,
                    'email': property.owner.email
                },
                'facilities': [{
                    'id': facility.id,
                    'name': facility.name
                } for facility in property.facilities],
                'created_at': property.created_at.isoformat(),
                'updated_at': property.updated_at.isoformat()
            }, 200
        except Exception as e:
            return {'error': str(e)}, 500

    @api.expect(property_model)
    @api.response(200, 'Property updated successfully')
    @api.response(404, 'Property not found')
    @api.response(400, 'Invalid input data')
    def put(self, property_id):
        """Update a property's information"""
        property_data = api.payload

        try:
            existing_property = facade.get_property(property_id)
            if not existing_property:
                return {'error': 'Property not found'}, 404

            if 'price_per_night' in property_data:
                if (not isinstance(property_data['price_per_night'], (int, float)) or property_data['price_per_night'] <= 0):
                    return {'error': 'Price must be a positive number'}, 400

            if 'latitude' in property_data:
                if (not isinstance(property_data['latitude'], (int, float)) or not (-90 <= property_data['latitude'] <= 90)):
                    return {'error': 'Latitude must be between -90 and 90'}, 400

            if 'longitude' in property_data:
                if (not isinstance(property_data['longitude'], (int, float)) or not (-180 <= property_data['longitude'] <= 180)):
                    return {'error': 'Longitude must be between -180 and 180'}, 400

            updated_property = facade.update_property(property_id, property_data)

            if not updated_property:
                return {'error': 'Property not found'}, 404
            return {
                'id': updated_property.id,
                'name': updated_property.name,
                'description': updated_property.description,
                'price_per_night': updated_property.price_per_night,
                'latitude': updated_property.latitude,
                'longitude': updated_property.longitude,
                'owner': {
                    'id': updated_property.owner.id,
                    'first_name': updated_property.owner.first_name,
                    'last_name': updated_property.owner.last_name,
                    'email': updated_property.owner.email
                },
                'facilities': [{
                    'id': facility.id,
                    'name': facility.name
                } for facility in updated_property.facilities],
                'created_at': updated_property.created_at.isoformat(),
                'updated_at': updated_property.updated_at.isoformat()
            }, 200

        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': str(e)}, 500


review_model = api.model('PropertyReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the property (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

property_with_reviews_model = api.model('PropertyWithReviews', {
    'name': fields.String(required=True, description='Name of the property'),
    'description': fields.String(description='Description of the property'),
    'price_per_night': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the property'),
    'longitude': fields.Float(required=True, description='Longitude of the property'),
    'owner': fields.Nested(owner_model, description='Owner of the property'),
    'facilities': fields.List(fields.Nested(facility_model), description='List of facilities'),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})
