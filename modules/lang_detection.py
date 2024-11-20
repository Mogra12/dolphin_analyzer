from langdetect import detect

class LangDetection:
    def __init__(self):
        self.detected_lang = None

    def lang_detection(self):
        with open("data/feedback.txt", "r") as src:
            text = src.read().strip()

        if not text:
            return "Error: The input text is empty."
        try:
            self.detected_lang = detect(text)
            if not self.detected_lang:
                return "Error: Language detection failed."
            return self.detected_lang
        except Exception as e:
            return f"Error during language detection: {str(e)}"
