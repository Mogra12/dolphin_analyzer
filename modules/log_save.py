import json
import re
from modules.stm_analyzer import StmAnalyzer
from datetime import datetime

def log():
    analyzer = StmAnalyzer()
    analyzer.analyze_sentiment()

    def clean_text(text):
        text = re.sub(r'\x1b\[[0-9;]*m', '', text)
        return text

    new_data = {
        "text": clean_text(analyzer.original_text),
        "sentiment": clean_text(analyzer.sentiment_returned),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
    }

    try:
        with open("data/database/database.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
            if isinstance(existing_data, dict):
                existing_data = [existing_data]
    except FileNotFoundError:
        existing_data = []
    except Exception as e:
        return f"Error: {e}"

    existing_data.append(new_data)

    with open("data/database/database.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4, ensure_ascii=False)
