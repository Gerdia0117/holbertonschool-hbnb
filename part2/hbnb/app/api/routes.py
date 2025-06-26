from flask import Flask, jsonify, request
from models.user import User
from models.place import Place

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'], password_hash=data['password_hash'])
    return jsonify(new_user.__dict__), 201

@app.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    new_place = Place(name=data['name'], city=data['city'], state=data['state'], description=data['description'], user_id=data['user_id'])
    return jsonify(new_place.__dict__), 201
