from flask import request, jsonify
from app.pets import bp
from app.pets import service as pets_service
from app.pets import schema as pets_schema


@bp.route('/pet', methods=['POST'])
def register_pet():
    schema = pets_schema.RegisterPetSchema()
    pet = schema.load(request.json)
    return jsonify(pets_schema.DetailsPetSchema().dump(pets_service.register_pet(pet))), 201
