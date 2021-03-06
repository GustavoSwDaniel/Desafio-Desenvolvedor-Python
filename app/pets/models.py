from app import db


class Pets(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)

    name_pet = db.Column(db.String(250), nullable=False)
    pet_owner_name = db.Column(db.String(250), nullable=False)
    breed = db.Column(db.String(250), nullable=False)
    birth_date = db.Column(db.String, nullable=False)
    pet_photo = db.Column(db.String, nullable=True)
