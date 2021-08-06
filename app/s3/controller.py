from flask import request

from app.commons.decoratios import validate_image_file
from app.pets import schema as pets_schema
from app.s3 import bp
from app.s3 import service as s3_service


@bp.route('/pet/photo/<int:pet_id>', methods=['POST'])
@validate_image_file
def upload_image(pet_id):
    file = request.files.get('file')
    pet = s3_service.upload_image(pet_id=pet_id, file=file)
    return pets_schema.DetailsPetSchema().dump(pet), 200
