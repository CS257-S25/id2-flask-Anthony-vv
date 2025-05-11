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
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to my ID2 Application!', response.data)

    def test_compare_valid_data(self):
        """Test the compare route with valid data."""
        response = self.app.get('/compare/2020-03-01/US,AF')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'COVID-19 data for 2020-03-01:', response.data)

    def test_compare_invalid_date_format(self):
        """Test the compare route with an invalid date format."""
        response = self.app.get('/compare/invalid-date/US,GB')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error:', response.data)

    def test_compare_invalid_country(self):
        """Test the compare route with a country code that likely doesn't exist."""
        response = self.app.get('/compare/2020-03-01/XYZ')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error:', response.data)

if __name__ == '__main__':
    unittest.main()
