#python
# Import necessary libraries
import unittest
import user_interface as ui
from unittest.mock import patch, Mock

class TestUserInterface(unittest.TestCase):

    @patch('flask.render_template')
    def test_home(self, mock_render):
        ui.home()
        mock_render.assert_called_once_with('home.html')

    @patch('flask.request')
    def test_get_user_data(self, mock_request):
        mock_request.form.get.side_effect = ['1', '25', '50000', 'rock']
        user_data = ui.get_user_data()
        expected_data = {
            'user_id': '1',
            'age': '25',
            'income': '50000',
            'preferences': 'rock'
        }
        self.assertEqual(user_data, expected_data)

    @patch('flask.render_template')
    def test_display_recommendations(self, mock_render):
        recommendations = ['rec1', 'rec2', 'rec3']
        ui.display_recommendations(recommendations)
        mock_render.assert_called_once_with('recommendations.html', recommendations=recommendations)

    @patch('flask.render_template')
    def test_display_history(self, mock_render):
        history = ['rec1', 'rec2', 'rec3']
        ui.display_history(history)
        mock_render.assert_called_once_with('history.html', history=history)

if __name__ == '__main__':
    unittest.main()

