import os

from mockito import when

from app.s3 import service as s3_service
from app.pets.models import Pets
from tests.base import BaseTestCase


class S3TestControllerCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        absolute_path = os.path.dirname(os.path.abspath(__file__))

        self.pet_image = {"file": open(f'{absolute_path}/file_test/download.jpeg', 'rb')}

        self.pet_with_image = Pets(id=1, name_pet='Mel', pet_owner_name='Gustavo',
                                   breed='siames', birth_date=2015, pet_photo='amazon.s3/mel.jpg')

    def test_update_image(self):
        when(s3_service).upload_image(...).thenReturn(self.pet_with_image)

        response = self.client().post('/pet/photo/1', content_type='multipart/form-data', data=self.pet_image, )
        response_json = response.get_data(as_text=True)

        self.assertIsNotNone(response.status_code, 200)
        self.assertIn('petPhoto', response_json)
