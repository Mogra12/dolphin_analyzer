from modules.stm_analyzer import StmAnalyzer
from modules.lang_detection import LangDetection
from modules.log_save import log
from modules.json_converter import json_to_pdf
from interface.interface_layout import layout
from colorama import Fore
from os import system, name
from json import load

class App:
    def run(self):
        # create sentiment analyzer instance
        analyzer = StmAnalyzer()
        langdetection = LangDetection()
        try:
            while True:
                layout()
                choose = int(input(f"{Fore.CYAN}➤ "))
                if choose == 1:
                    # clear console screen
                    if name == "posix":
                        system("clear")
                    else:
                        system("cls")

                    # analyze sentiment
                    sentiment = analyzer.analyze_sentiment()

                    # result of analyze
                    print(f"{Fore.BLUE}+" * 100)
                    print(f"{Fore.WHITE}Language: {Fore.GREEN}{langdetection.lang_detection()}")
                    print(f"{Fore.WHITE}The sentiment of the given text is: {sentiment}")
                    print(f"{Fore.BLUE}+" * 100)

                    # save log
                    log()

                elif choose == 2:
                    with open('data/database/database.json', 'r') as f:
                        json_data = load(f)
                    json_to_pdf(json_data, 'log_db.pdf')
                    print(f"{Fore.LIGHTGREEN_EX}\nLog saved as log_db.pdf!")
                elif choose == 0:
                    print("Exiting the program...")
                    break

        except KeyboardInterrupt:
            print("\tProgram interrupted by user.")
        #except Exception:
        #    print(f"An error occurred")


if "__main__" == __name__:
    app = App()
    app.run()
