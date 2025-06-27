from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import facade

api = Namespace('facilities', description='Facility management operations')

facility_model = api.model('Facility', {
    'name': fields.String(required=True, description='Name of the facility')
})

@api.route('/')
class FacilityList(Resource):
    @api.expect(facility_model)
    @api.response(201, 'Facility successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Add a new facility"""
        facility_data = api.payload

        if not facility_data or 'name' not in facility_data:
            return {'error': 'Missing required field: name'}, 400

        if not facility_data['name'].strip():
            return {'error': 'Name cannot be empty'}, 400

        try:

            new_facility = facade.add_facility(facility_data)
            return {
                'id': new_facility.id,
                'name': new_facility.name,
                'created_at': new_facility.created_at.isoformat(),
                'updated_at': new_facility.updated_at.isoformat()
            }, 201
        except Exception as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of facilities retrieved successfully')
    def get(self):
        """Fetch a list of all facilities"""
        try:
            facilities = facade.get_all_facilities()
            return [
                {
                    'id': facility.id,
                    'name': facility.name,
                    'created_at': facility.created_at.isoformat(),
                    'updated_at': facility.updated_at.isoformat()
                }
                for facility in facilities
            ], 200
        except Exception as e:
            return {'error': str(e)}, 500


@api.route('/<facility_id>')
class FacilityResource(Resource):
    @api.response(200, 'Facility details retrieved successfully')
    @api.response(404, 'Facility not found')
    def get(self, facility_id):
        """Get facility details by ID"""
        try:
            facility = facade.get_facility(facility_id)
            if not facility:
                return {'error': 'Facility not found'}, 404

            return {
                'id': facility.id,
                'name': facility.name,
                'created_at': facility.created_at.isoformat(),
                'updated_at': facility.updated_at.isoformat()
            }, 200
        except Exception as e:
            return {'error': str(e)}, 500

    @api.expect(facility_model)
    @api.response(200, 'Facility updated successfully')
    @api.response(404, 'Facility not found')
    @api.response(400, 'Invalid input data')
    def put(self, facility_id):
        """Update a facility's information"""
        pass
