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

    def test_register_pet(self):
        with self.app.app_context():
            response = pets_service.register_pet(self.pets_register)

            self.assertIsInstance(response, Pets)

    def test_get_pet_by_id(self):
        with self.app.app_context():
            response = pets_service.get_pet_by_id(2)

            self.assertIsInstance(response, Pets)

    def test_get_pet_by_id_does_not_found(self):
        with self.app.app_context():
            self.assertRaises(ObjectDoesNotFoundError, pets_service.get_pet_by_id, 500)
