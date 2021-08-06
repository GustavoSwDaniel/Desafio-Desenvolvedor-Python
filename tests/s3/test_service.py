import os

from mockito import when

from app.pets.models import Pets
from tests.base import BaseTestCase
from app.s3.client import S3client
from app.s3 import service as s3_service


class S3TestServiceCase(BaseTestCase):
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

    def test_upload_file(self):
        class File:
            def __init__(self, key, value, content_type, filename):
                self.key = key
                self.value = value
                self.content_type = content_type
                self.filename = filename

        absolute_path = os.path.dirname(os.path.abspath(__file__))

        file = File(
            key='file',
            value=open(f'{absolute_path}/file_test/download.jpeg', 'rb'),
            content_type='image/png',
            filename='download.jpeg'
        )

        file_url_return = f'https://amazonaws.com/1/image/download.jpeg'
        when(S3client).upload_file(...).thenReturn(file_url_return)

        with self.app.app_context():
            response = s3_service.upload_image(self.pets_registered.id, file=file)

            self.assertIsInstance(response, Pets)
            self.assertEqual(file_url_return, response.pet_photo)
