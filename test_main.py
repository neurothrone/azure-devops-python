"""
Unit tests for the Flask app.
"""

import unittest
from main import app


class TestMain(unittest.TestCase):
    """Test case for verifying the Flask app routes."""

    def test_home_route(self):
        """Tests if the home route returns the expected response."""
        tester = app.test_client()
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Azure DevOps Dev", response.data.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
