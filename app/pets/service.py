from app import db
from app.pets.models import Pets
from werkzeug.security import generate_password_hash
from app.commons.exceptions import ObjectDoesNotFoundError


def register_pet(pet: Pets) -> Pets:
    db.session.add(pet)
    db.session.commit()
    return pet


def get_pet_by_id(pet_id: int) -> Pets:
    pet = Pets.query.filter_by(id=pet_id).first()
    if pet:
        return pet

    raise ObjectDoesNotFoundError(message="Pet does not found")
