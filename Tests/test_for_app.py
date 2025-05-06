"""Unit tests for the Flask application for COVID-19 stats comparison"""

import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    """Unit tests for the Flask application"""
    def setUp(self):
        """Set up the test client for the Flask application."""
        self.app = app.test_client()

    def test_homepage(self):
        """Test the homepage route."""
        response = self.app.get('/')
        self.assertIn(b'Welcome to my ID2 Application!', response.data)

    def test_compare_valid_data(self):
        """Test the compare route with valid data."""
        response = self.app.get('/compare/2020-03-01/US,AF')
        self.assertIn(b'COVID-19 data for 2020-03-01:', response.data)

    # Uncomment and implement this test if needed
    # def test_compare_invalid_date(self):
    #     """Test the compare route with an invalid date."""
    #     response = self.app.get('/compare/invalid-date/US,GB')
    #     self.assertIn(b'Error:', response.data)

if __name__ == '__main__':
    unittest.main()
