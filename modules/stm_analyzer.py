from deep_translator import GoogleTranslator
from textblob import TextBlob
from colorama import Fore
from langdetect import detect

class StmAnalyzer:
    def __init__(self):
        self.sentiment_returned = None
        self.original_text = None
        
    def analyze_sentiment(self):
        __MAX_LENGTH = 1000
        with open("data/feedback.txt", "r") as src:
            text = src.read().strip()

        self.original_text = text
        
        # Check if text is too long and if text is empty or none
        if len(text) > __MAX_LENGTH:
            return "Error: The input text is too long. Maximum length is 1000 characters."
        elif not text:
            return "Error: The input text is empty."

        try:
            # Detect the language of the input text
            detected_lang = detect(text)
            # If the text is not in English, translate it to English
            if detected_lang != "en":
                translated_text = GoogleTranslator(source="auto", target="en").translate(text)
            else:
                translated_text = text
        except Exception as e:
            return f"Error during translation: {str(e)}"
        
        try:
            # Correct any spelling mistakes in the text
            blob = TextBlob(translated_text)
            spelled_text = blob.correct()
            sentiment = spelled_text.sentiment

            # Check if sentiment is valid
            if sentiment is None:
                return "Error: Sentiment analysis failed."

            # Return sentiment based on polarity
            match sentiment.polarity:
                case polarity if polarity <= -0.5:
                    sentiment_return = f"{Fore.RED}Extremely Negative ☆☆☆☆☆☆"
                case polarity if -0.4 <= polarity < 0:
                    sentiment_return = f"{Fore.YELLOW}Negative ★☆☆☆☆☆"
                case polarity if 0 <= polarity < 0.3:
                    sentiment_return = f"{Fore.WHITE}Neutral ★★★☆☆☆"
                case polarity if 0.4 <= polarity < 0.6:
                    sentiment_return = f"{Fore.LIGHTGREEN_EX}Positive ★★★★☆☆"
                case polarity if 0.6 <= polarity <= 0.7:
                    sentiment_return = f"{Fore.GREEN}Very Positive ★★★★★☆"
                case polarity if 0.7 < polarity <= 1:
                    sentiment_return = f"{Fore.GREEN}Extremely Positive ★★★★★★"

            # Atribuindo o sentimento à variável da instância antes de retornar
            self.sentiment_returned = sentiment_return

            return sentiment_return

        except Exception as e:
            return f"Error: {e}"
