import unittest
from flask import json
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_image(self):
        response = self.app.get('/get-image')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('image_url', data)

if __name__ == '__main__':
    unittest.main()