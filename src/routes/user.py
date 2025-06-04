from models.User import User
from flask import Blueprint, jsonify
from database.db import db

api = Blueprint('api/user', __name__)

@api.route('/', methods=['GET'])
def get_users():
    all_user = User.query.all()
    all_user_serialize = list(map(lambda user: user.serialize(), all_user))
    return jsonify(all_user_serialize), 200