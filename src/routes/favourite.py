from models.Favourites import Favourite
from models.Login import Login
from flask import Blueprint, jsonify
from database.db import db
from models.Planet import Planet
from models.Character import Character

api = Blueprint('api/favourite', __name__)

@api.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    current_login = Login.query.filter_by(user_login=True).first()
    if not current_login:
        return jsonify({"error": "usuario NO logueado"}), 401
    
    user_favorites = Favourite.query.filter_by(user_id=current_login.user_id).all()
    favorites_serialized = list(map(lambda fav: fav.serialize(), user_favorites))
    return jsonify(favorites_serialized), 200

@api.route('/favourite/planet/<int:planet_id>', methods=['POST'])
def add_planet_favourite(planet_id):
    current_login = Login.query.filter_by(user_login=True).first()
    if not current_login:
        return jsonify({"error": "usuario NO logueado"}), 401

    planet = Planet.query.get(planet_id)
    if not planet:
        return jsonify({"error": "Planeta NO encontrado"}), 404

    existing_favourite = Favourite.query.filter_by(
        user_id=current_login.user_id,
        planet_id=planet_id
    ).first()
    if existing_favourite:
        return jsonify({"error": "Planeta en favoritos"}), 400
    
    new_favourite = Favourite(
        user_id=current_login.user_id,
        planet_id=planet_id,
        login_id=current_login.id
    )
    
    db.session.add(new_favourite)
    db.session.commit()
    
    return jsonify(new_favourite.serialize()), 201

@api.route('/favourite/character/<int:character_id>', methods=['POST'])
def add_character_favourite(character_id):
    current_login = Login.query.filter_by(user_login=True).first()
    if not current_login:
        return jsonify({"error": "usuario NO logueado"}), 401
    
    character = Character.query.get(character_id)
    if not character:
        return jsonify({"error": "Personaje NO encontrado"}), 404
    
    existing_favourite = Favourite.query.filter_by(
        user_id=current_login.user_id,
        character_id=character_id
    ).first()
    if existing_favourite:
        return jsonify({"error": "Personaje en favoritos"}), 400
    
    new_favourite = Favourite(
        user_id=current_login.user_id,
        character_id=character_id,
        login_id=current_login.id
    )
    
    db.session.add(new_favourite)
    db.session.commit()
    
    return jsonify(new_favourite.serialize()), 201

@api.route('/favourite/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet_favourite(planet_id):
    current_login = Login.query.filter_by(user_login=True).first()
    if not current_login:
        return jsonify({"error": "usuario NO logueado"}), 401
    
    favourite = Favourite.query.filter_by(
        user_id=current_login.user_id,
        planet_id=planet_id
    ).first()
    if not favourite:
        return jsonify({"error": "Planeta NO en favoritos"}), 404
    
    db.session.delete(favourite)
    db.session.commit()
    
    return jsonify({"message": "Planeta eliminado"}), 200

@api.route('/favourite/character/<int:character_id>', methods=['DELETE'])
def delete_character_favourite(character_id):
    current_login = Login.query.filter_by(user_login=True).first()
    if not current_login:
        return jsonify({"error": "usuario NO logueado"}), 401
    
    favourite = Favourite.query.filter_by(
        user_id=current_login.user_id,
        character_id=character_id
    ).first()
    if not favourite:
        return jsonify({"error": "Personaje NO en favoritos"}), 404
    
    db.session.delete(favourite)
    db.session.commit()
    
    return jsonify({"message": "Personaje eliminado"}), 200
