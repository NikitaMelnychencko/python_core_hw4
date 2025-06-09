from colorama import Fore

def log_folder(message):
    print(f"{Fore.BLUE} {message}")

def log_file(message):
    print(f"{Fore.YELLOW} {message}")

def log_error(message):
    print(f"{Fore.RED} [ERROR] {Fore.RESET} {message}")