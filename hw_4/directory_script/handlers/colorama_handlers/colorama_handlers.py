from colorama import Fore, Style

def main_dir_colored(message):
    print(f"{Fore.CYAN}DIR NAME: {message}{Fore.RESET}")

def exept_colored(message):
    print(f"{Fore.RED}WARNING: {message}{Fore.RESET}")

def file_colored(message):
    return f"{Fore.GREEN}[F]{Fore.RESET} {message}"

def dir_colored(message):
    return f"{Fore.YELLOW}[D]{Fore.RESET} {message}"

def dir_tree_slyled(i):
    return f"{Style.DIM}{'|' * i + '-'}{Style.RESET_ALL}"

