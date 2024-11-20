from json import dump, load
from re import sub
from modules.stm_analyzer import StmAnalyzer
from datetime import datetime

def log():
    try:
        # create sentiment analyzer instance
        analyzer = StmAnalyzer()
        analyzer.analyze_sentiment()

        def clean_text(text):
            # remove ANSI escape sequences from the text
            text = sub(r'\x1b\[[0-9;]*m', '', text)
            return text

        # create a dictionary with the original text, sentiment, and timestamp
        new_data = {
            "text": clean_text(analyzer.original_text),
            "sentiment": clean_text(analyzer.sentiment_returned),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
        }

        try:
            # read existing data from the database file
            with open("data/database/database.json", "r", encoding="utf-8") as file:
                existing_data = load(file)
                if isinstance(existing_data, dict):
                    existing_data = [existing_data]
        except FileNotFoundError:
            existing_data = []
        except Exception as e:
            return f"Error: {e}"

        existing_data.append(new_data)

        # Dump json file with data
        with open("data/database/database.json", "w", encoding="utf-8") as file:
            dump(existing_data, file, indent=4, ensure_ascii=False)
    except KeyboardInterrupt:
        return "Program interrupted by user."