import colorama
from colorama import Fore, Style

def get_funny_message():
    return f"Azure DevOps -> {Fore.YELLOW}Warning: Low battery! Please charge your developer...{Style.RESET_ALL}"

def main():
    colorama.init()
    print(get_funny_message())
    
if __name__ == "__main__":
    main()