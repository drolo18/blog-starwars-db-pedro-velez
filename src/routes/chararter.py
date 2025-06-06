from models.Character import Character
from flask import Blueprint, jsonify, request
from database.db import db

api = Blueprint('api/character', __name__)

@api.route('/', methods=['GET'])
def get_characters():
    all_characters = Character.query.all()
    characters_serialized = list(map(lambda character: character.serialize(), all_characters))
    return jsonify(characters_serialized), 200

@api.route('/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = Character.query.get(character_id)
    if character is None:
        return jsonify({"error": "Personaje NO encontrado"}), 404
    return jsonify(character.serialize()), 200

@api.route('/', methods=['POST'])
def create_character():
    body = request.get_json()
    
    if body is None:
        return jsonify({"error": "Datos NO enviados"}), 400
    
    if "character_name" not in body:
        return jsonify({"error": "Datos incompletos"}), 400
    
    existing_character = Character.query.filter_by(character_name=body["character_name"]).first()
    if existing_character:
        return jsonify({"error": "Personaje ya existe"}), 400
    
    new_character = Character(
        character_name=body["character_name"]
    )
    
    db.session.add(new_character)
    db.session.commit()
    
    return jsonify(new_character.serialize()), 201

@api.route('/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):
    character = Character.query.get(character_id) 
    if character is None:
        return jsonify({"error": "Personaje NO encontrado"}), 404
    
    db.session.delete(character)
    db.session.commit()
    
    return jsonify({"message": "Personaje eliminado"}), 200
