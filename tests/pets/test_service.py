from tests.base import BaseTestCase
from app.pets.models import Pets
from app.pets import service as pets_service
from app.commons.exceptions import ObjectDoesNotFoundError


class PetsTestServiceCase(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.pets_register = Pets(id=1, name_pet='LILI', pet_owner_name='Gustavo',
                                  breed='siamês', birth_date='2017')

        self.pets_registered = Pets(id=2, name_pet='Fred', pet_owner_name='Amanda',
                                    breed='salsicha', birth_date='2016')

        with self.app.app_context():
            self.db.session.add(self.pets_registered)
            self.db.session.commit()

            self.db.session.refresh(self.pets_registered)
            self.db.session.expunge(self.pets_registered)

    def test_save_pet(self):
        with self.app.app_context():
            response = pets_service.save_pet(self.pets_register)

            self.assertIsInstance(response, Pets)

    def test_get_pet_by_id(self):
        with self.app.app_context():
            response = pets_service.get_pet_by_id(2)

            self.assertIsInstance(response, Pets)

    def test_get_pet_by_id_does_not_found(self):
        with self.app.app_context():
            self.assertRaises(ObjectDoesNotFoundError, pets_service.get_pet_by_id, 500)

    def test_update_pets(self):
        update_date = {
            'pet_owner_name': 'Gustavo D'
        }
        with self.app.app_context():
            response = pets_service.update_pet(2, update_date)

            self.assertNotEqual(response.pet_owner_name, self.pets_registered.pet_owner_name)
            self.assertEqual(response.pet_owner_name, update_date['pet_owner_name'])

    def test_remove_pets(self):
        with self.app.app_context():
            response = pets_service.get_pet_by_id(2)

            self.assertIsInstance(response, Pets)

            pets_service.remove_pet(2)

            self.assertRaises(ObjectDoesNotFoundError, pets_service.get_pet_by_id, 2)

    def test_remove_pet_with_pet_does_not_found(self):
        with self.app.app_context():
            self.assertRaises(ObjectDoesNotFoundError, pets_service.remove_pet, 100)
