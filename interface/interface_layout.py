from colorama import Fore

def layout():
    # Define the layout for the sentiment analysis application
    layout = f"""
    {Fore.CYAN}
    ▓█████▄  ▒█████   ██▓     ██▓███   ██░ ██  ██▓ ███▄    █
    ▒██▀ ██▌▒██▒  ██▒▓██▒    ▓██░  ██▒▓██░ ██▒▓██▒ ██ ▀█   █
    ░██   █▌▒██░  ██▒▒██░    ▓██░ ██▓▒▒██▀▀██░▒██▒▓██  ▀█ ██▒
    ░▓█▄   ▌▒██   ██░▒██░    ▒██▄█▓▒ ▒░▓█ ░██ ░██░▓██▒  ▐▌██▒
    ░▒████▓ ░ ████▓▒░░██████▒▒██▒ ░  ░░▓█▒░██▓░██░▒██░   ▓██░
    ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░▓  ░▒▓▒░ ░  ░ ▒ ░░▒░▒░▓  ░ ▒░   ▒ ▒
    ░ ▒  ▒   ░ ▒ ▒░ ░ ░ ▒  ░░▒ ░      ▒ ░▒░ ░ ▒ ░░ ░░   ░ ▒░
    ░ ░  ░ ░ ░ ░ ▒    ░ ░   ░░        ░  ░░ ░ ▒ ░   ░   ░ ░
    ░        ░ ░      ░  ░          ░  ░  ░ ░           ░
    
    {Fore.WHITE}This script is designed to analyze the sentiment of a given text using the {Fore.CYAN}TextBlob {Fore.WHITE}library.
    {Fore.CYAN}Github: {Fore.WHITE}https://github.com/Mogra12/dolphin_analyzer
    {Fore.RED}Enter 0 to exit
    
    {Fore.CYAN}1 {Fore.WHITE}- Sentiment Analyzer
    {Fore.CYAN}2 {Fore.WHITE}- Save log file in PDF
    """
    print(layout)