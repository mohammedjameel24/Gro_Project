#python
# Import necessary libraries
import unittest
import main as m
import json

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = m.app.test_client()
        self.app.testing = True

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_recommend(self):
        user_data = {
            'user_id': 1,
            'age': 25,
            'income': 50000,
            'genre': 'rock'
        }
        result = self.app.post('/recommend', data=json.dumps(user_data), content_type='application/json')
        self.assertEqual(result.status_code, 200)
        self.assertTrue('recommendations' in result.get_json())

    def test_history(self):
        result = self.app.get('/history?user_id=1')
        self.assertEqual(result.status_code, 200)
        self.assertTrue('history' in result.get_json())

if __name__ == '__main__':
    unittest.main()

