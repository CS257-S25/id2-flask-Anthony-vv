"""Unit tests for the Flask application for COVID-19 stats comparison"""

import unittest
from unittest.mock import patch
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
        with patch('ProductionCode.covid_stats.stats') as mock_stats:
            mock_stats.return_value = (100, 5)
            # Break the line further to avoid exceeding the length limit
            response = self.app.get(
                '/compare/2020-03-01/'  # URL part 1
                'US,AF'  # URL part 2
            ) 
            self.assertIn(b'COVID-19 data for 2020-03-01:', response.data)
            self.assertIn(b'US: Cases=100, Deaths=5', response.data)
            self.assertIn(b'AF: Cases=100, Deaths=5', response.data)

    def test_compare_invalid_country(self):
        """Test the compare route with an invalid country to trigger error handling."""
        with patch('ProductionCode.covid_stats.stats', side_effect=KeyError("Invalid country code")):
            response = self.app.get('/compare/2020-03-01/INVALID')
            self.assertIn(b'Error: Invalid country code', response.data)

if __name__ == '__main__':
    unittest.main()
