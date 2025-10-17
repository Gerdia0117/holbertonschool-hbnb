from flask_restx import Namespace, Resource, fields
from app.services.storage_service import storage

api = Namespace('users', description='User related operations')

user_model = api.model('User', {
    'id': fields.String(readOnly=True),
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'email': fields.String(required=True),
})

@api.route('/')
class UserList(Resource):
    def get(self):
        users = storage.get_all('User')
        return [u.to_dict() for u in users], 200

