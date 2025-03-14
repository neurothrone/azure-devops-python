"""
Unit tests for the main script.
"""

import unittest
from colorama import Fore, Style
from main import get_funny_message


class TestMain(unittest.TestCase):
    """Test case for verifying the get_funny_message function."""

    def test_get_funny_message(self):
        """Tests if get_funny_message returns the expected formatted string."""
        expected_output = (
            f"Azure DevOps Dev -> {Fore.YELLOW}Warning: Low battery! "
            f"Please charge your developer...{Style.RESET_ALL}"
        )
        self.assertEqual(get_funny_message(), expected_output)


if __name__ == "__main__":
    unittest.main()
