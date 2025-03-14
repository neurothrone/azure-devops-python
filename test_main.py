import unittest
from main import get_funny_message
from colorama import Fore, Style

class TestMain(unittest.TestCase):
    def test_get_funny_message(self):
        expected_output = f"Azure DevOps -> {Fore.YELLOW}Warning: Low battery! Please charge your developer...{Style.RESET_ALL}"
        self.assertEqual(get_funny_message(), expected_output)

if __name__ == "__main__":
    unittest.main()
