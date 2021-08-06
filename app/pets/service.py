from app import db, pets
from app.pets.models import Pets
from werkzeug.security import generate_password_hash
from app.commons.exceptions import ObjectDoesNotFoundError


def save_pet(pet: Pets) -> Pets:
    db.session.add(pet)
    db.session.commit()
    return pet


def get_pet_by_id(pet_id: int) -> Pets:
    pet = Pets.query.filter_by(id=pet_id).first()
    if pet:
        return pet

    raise ObjectDoesNotFoundError(message="Pet does not found")


def update_pet(pet_id: int, update_date: dict) -> Pets:
    pet_data = get_pet_by_id(pet_id=pet_id)

    editable_attributes = ['name_pet', 'pet_owner_name', 'breed', 'birth_date']

    list(map(lambda attribute: setattr(pet_data, attribute, update_date[attribute]), filter(
        lambda element: element in update_date, editable_attributes)))

    db.session.add(pet_data)
    db.session.commit()
    return pet_data


def remove_pet(pet_id: int):
    pet = get_pet_by_id(pet_id=pet_id)

    db.session.delete(pet)
    db.session.commit()
