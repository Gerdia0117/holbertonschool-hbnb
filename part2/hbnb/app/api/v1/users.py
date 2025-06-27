from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('customers', description='Customer operations')

customer_model = api.model('Customer', {
    'first_name': fields.String(required=True, description='First name of the customer'),
    'last_name': fields.String(required=True, description='Last name of the customer'),
    'email': fields.String(required=True, description='Email of the customer')
})


@api.route('/')
class CustomerList(Resource):
    @api.response(200, 'List of customers retrieved successfully')
    def get(self):
        """Retrieve a list of all customers"""
        try:
            customers = facade.get_all_customers()
            return [{'id': customer.id, 'first_name': customer.first_name,
                     'last_name': customer.last_name, 'email': customer.email} for customer in customers], 200
        except Exception as e:
            return {'error': str(e)}, 500

    @api.expect(customer_model, validate=True)
    @api.response(201, 'Customer successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new customer"""
        customer_data = api.payload

        existing_customer = facade.get_customer_by_email(customer_data['email'])
        if existing_customer:
            return {'error': 'Email already registered'}, 400

        try:
            new_customer = facade.create_customer(customer_data)
            return {
                'id': new_customer.id,
                'first_name': new_customer.first_name,
                'last_name': new_customer.last_name,
                'email': new_customer.email
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': 'An unexpected error occurred'}, 500


@api.route('/<customer_id>')
class CustomerResource(Resource):
    @api.response(200, 'Customer details retrieved successfully')
    @api.response(404, 'Customer not found')
    def get(self, customer_id):
        """Get customer details by ID"""
        try:
            customer = facade.get_customer(customer_id)
            if not customer:
                return {'error': 'Customer not found'}, 404
            return {
                'id': customer.id,
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                'email': customer.email
            }, 200
        except Exception as e:
            return {'error': str(e)}, 500

    @api.expect(customer_model, validate=True)
    @api.response(200, 'Customer successfully updated')
    @api.response(404, 'Customer not found')
    @api.response(400, 'Invalid input data')
    def put(self, customer_id):
        """Update a customer's information"""
        customer_data = api.payload

        try:
            customer = facade.get_customer(customer_id)
            if not customer:
                return {'error': 'Customer not found'}, 404

            if 'email' in customer_data and customer_data['email'] != customer.email:
                existing_customer = facade.get_customer_by_email(customer_data['email'])
                if existing_customer:
                    return {'error': 'Email already registered'}, 400

            updated_customer = facade.update_customer(customer_id, customer_data)
            return {
                'id': updated_customer.id,
                'first_name': updated_customer.first_name,
                'last_name': updated_customer.last_name,
                'email': updated_customer.email
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': 'An unexpected error occurred'}, 500
