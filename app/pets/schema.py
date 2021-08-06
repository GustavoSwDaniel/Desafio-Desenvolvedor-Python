from marshmallow import Schema, fields, post_load
from app.pets.models import Pets


class RegisterPetSchema(Schema):
    name_pet = fields.String(required=True, data_key='namePets')
    pet_owner_name = fields.String(required=True, data_key='petOwnerName')
    breed = fields.String(required=True)
    birth_date = fields.String(required=True, data_key='birthDate')

    @post_load
    def make_pet(self, data, **kwargs):
        return Pets(**data)


class DetailsPetSchema(Schema):
    name_pet = fields.String(data_key='namePets')
    pet_owner_name = fields.String(data_key='petOwnerName')
    breed = fields.String()
    birth_date = fields.String(data_key='birthDate')
    pet_photo = fields.String(data_key='petPhoto')


class UpdatePetSchema(Schema):
    name_pet = fields.String(data_key='namePets')
    pet_owner_name = fields.String(data_key='petOwnerName')
    breed = fields.String()
    birth_date = fields.String(data_key='birthDate')
