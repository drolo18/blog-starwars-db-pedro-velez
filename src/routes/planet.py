from models.Planet import Planet
from flask import Blueprint, jsonify, request
from database.db import db

api = Blueprint('api/planet', __name__)

@api.route('/', methods=['GET'])
def get_planets():
    all_planets = Planet.query.all()  
    planets_serialized = list(map(lambda planet: planet.serialize(), all_planets))
    return jsonify(planets_serialized), 200


@api.route('/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify({"error": "Planeta NO encontrado"}), 404
    return jsonify(planet.serialize()), 200

@api.route('/', methods=['POST'])
def create_planet():
    body = request.get_json()
    
    if body is None:
        return jsonify({"error": "Datos NO enviados"}), 400
    
    if "Planet_name" not in body:
        return jsonify({"error": "Datos incompletos"}), 400
    
    existing_planet = Planet.query.filter_by(Planet_name=body["Planet_name"]).first()
    if existing_planet:
        return jsonify({"error": "Planeta ya existe"}), 400
    
    new_planet = Planet(
        Planet_name=body["Planet_name"]
    )
    
    db.session.add(new_planet)
    db.session.commit()
    
    return jsonify(new_planet.serialize()), 201

@api.route('/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify({"error": "Planeta NO encontrado"}), 404
    
    db.session.delete(planet)
    db.session.commit()
    
    return jsonify({"message": "Planeta eliminado"}), 200