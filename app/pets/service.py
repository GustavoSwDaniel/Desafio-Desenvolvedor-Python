from app import db
from app.pets.models import Pets
from werkzeug.security import generate_password_hash


def register_pet(pet: Pets) -> Pets:
    db.session.add(pet)
    db.session.commit()
    return pet
