from models.User import User
from flask import Blueprint, jsonify, request
from database.db import db
import datetime

api = Blueprint('api/user', __name__)

@api.route('/', methods=['GET'])
def get_users():
    all_user = User.query.all()
    all_user_serialize = list(map(lambda user: user.serialize(), all_user))
    return jsonify(all_user_serialize), 200

@api.route('/', methods=['POST'])
def create_user():
    body = request.get_json()
    if body is None:
        return jsonify({"error": "Datos NO enviados"}), 400
    
    if "user_name" not in body or "first_name" not in body or "last_name" not in body or "email" not in body or "pasword" not in body:
        return jsonify({"error": "Datos incompletos"}), 400
    
    existing_user = User.query.filter_by(user_name=body["user_name"]).first()
    if existing_user:
        return jsonify({"error": "Usuario ya existe"}), 400
    
    existing_email = User.query.filter_by(email=body["email"]).first()
    if existing_email:
        return jsonify({"error": "Email ya registrado"}), 400
    
    new_user = User(
        user_name=body["user_name"],
        first_name=body["first_name"],
        last_name=body["last_name"],
        email=body["email"],
        pasword=body["pasword"],
        date=datetime.datetime.now()
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(new_user.serialize()), 201
