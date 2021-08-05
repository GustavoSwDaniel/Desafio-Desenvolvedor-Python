from tests.base import BaseTestCase
from app.pets.models import Pets
from app.pets import service as pets_service


class PetsTestServiceCase(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.pets_register = Pets(id=1, name_pet='LILI', pet_owner_name='Gustavo',
                                  breed='siamês', birth_date='2017')

    def test_register_pet(self):
        with self.app.app_context():
            response = pets_service.register_pet(self.pets_register)

            self.assertIsInstance(response, Pets)
