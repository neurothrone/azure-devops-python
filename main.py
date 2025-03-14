"""
A simple script that prints a funny message with color.
"""

import colorama
from colorama import Fore, Style


def get_funny_message():
    """Returns a funny, colored message with a prefix."""
    return (
        f"Azure DevOps Dev -> {Fore.YELLOW}Warning: Low battery! "
        f"Please charge your developer...{Style.RESET_ALL}"
    )


def main():
    """Main function to print the funny message."""
    colorama.init()
    print(get_funny_message())


if __name__ == "__main__":
    main()
