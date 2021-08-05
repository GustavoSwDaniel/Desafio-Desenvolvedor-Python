from flask import request, jsonify
from werkzeug.exceptions import abort

from app.commons.exceptions import ObjectDoesNotFoundError
from app.pets import bp
from app.pets import schema as pets_schema
from app.pets import service as pets_service


@bp.route('/pet', methods=['POST'])
def register_pet():
    schema = pets_schema.RegisterPetSchema()
    pet = schema.load(request.json)
    return jsonify(pets_schema.DetailsPetSchema().dump(pets_service.register_pet(pet))), 201


@bp.route('/pet/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    try:
        return jsonify(pets_schema.DetailsPetSchema().dump(pets_service.get_pet_by_id(pet_id))), 200
    except ObjectDoesNotFoundError as error:
        abort(404, error.message)
