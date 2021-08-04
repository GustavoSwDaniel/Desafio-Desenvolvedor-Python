from app import db


class Pets(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name_pet = db.Column(db.String(250), nullable=True)
    pet_owner_name = db.Column(db.String(250), nullable=True)
    breed = db.Column(db.String(250), nullable=True)
    birth_date = db.Column(db.String, nullable=True)