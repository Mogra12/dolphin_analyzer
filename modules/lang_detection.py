from langdetect import detect

class LangDetection:
    def __init__(self):
        self.detected_lang = None

    def lang_detection(self):
        try:
            # read text from the feedback file
            with open("data/feedback.txt", "r") as src:
                text = src.read().strip()

            # check text is empty
            if not text:
                return "Error: The input text is empty."
            try:
                # detect the language of the input text and store it in the class attribute
                self.detected_lang = detect(text)
                if not self.detected_lang:
                    return "Error: Language detection failed."
                return self.detected_lang
            except Exception as e:
                return f"Error: {str(e)}"
        except KeyboardInterrupt:
            return "Interrupted by user."
