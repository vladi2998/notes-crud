import unittest
from app import create_app

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_create_note(self):
        response = self.client.post('/notes', json={'title': 'Test Note', 'content': 'This is a test note.'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_notes(self):
        response = self.client.get('/notes')
        self.assertEqual(response.status_code, 200)

    def test_get_note_by_id(self):
        response = self.client.post('/notes', json={'title': 'Test Note', 'content': 'This is a test note.'})
        note_id = response.get_json()['id']
        response = self.client.get(f'/notes/{note_id}')
        self.assertEqual(response.status_code, 200)

    def test_update_note(self):
        response = self.client.post('/notes', json={'title': 'Test Note', 'content': 'This is a test note.'})
        note_id = response.get_json()['id']
        response = self.client.put(f'/notes/{note_id}', json={'title': 'Updated Note', 'content': 'Updated content.'})
        self.assertEqual(response.status_code, 200)

    def test_delete_note(self):
        response = self.client.post('/notes', json={'title': 'Test Note', 'content': 'This is a test note.'})
        note_id = response.get_json()['id']
        response = self.client.delete(f'/notes/{note_id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
