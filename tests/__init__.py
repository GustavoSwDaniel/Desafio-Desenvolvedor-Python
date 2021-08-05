import unittest

from mockito import unstub

from app import create_app, db


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.db = db

        with self.app.app_context():

            # Remove mocks
            unstub()

            self.db.create_all()