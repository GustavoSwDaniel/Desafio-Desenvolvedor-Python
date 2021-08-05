import json

from tests.base import BaseTestCase
from app.pets.models import Pets
from app.pets import service as pets_service
from mockito import when


class PetsTestControllerCase(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.pets_register = Pets(id=1, name_pet='LILI', pet_owner_name='Gustavo',
                                  breed='siamês', birth_date='2017')

    def test_register_pet(self):
        self.data = {
                'namePets': 'Gustavo',
                'petOwnerName': 'Mel',
                'breed': 'ciames',
                'birthDate': '2017'
            }
        when(pets_service).register_pet(...).thenReturn(self.pets_register)
        response = self.client().post('/pet', data=json.dumps(self.data),
                                      content_type='application/json')
        response_json = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 201)
        self.assertIn('birthDate', response_json)
        self.assertIn('breed', response_json)
        self.assertIn('namePets', response_json)
        self.assertIn('petOwnerName', response_json)
