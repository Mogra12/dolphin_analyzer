import textblob as tb
from translate import 

class StmAnalyzer:
      def __init__(self):
            pass
      def analyze_sentiment(self,text):
            # Use TextBlob's sentiment analyzer to get the sentiment of the text
            blob = tb.TextBlob(text)

            # Correct any spelling mistakes in the text using TextBlob's correct() method
            spelled_text = blob.correct()
            sentiment = spelled_text.sentiment
            # Return the sentiment as a string
            match sentiment.polarity:
                  case polarity if polarity <= -0.3:
                        return 'Extremely Negative ☆☆☆☆☆☆'
                  case polarity if -0.3 < polarity < 0:
                        return 'Negative ★☆☆☆☆☆'
                  case polarity if 0 <= polarity < 0.2:
                        return 'Neutral ★★★☆☆☆'
                  case polarity if 0.2 <= polarity < 0.6:
                        return 'Gently Positive ★★★★☆☆'
                  case polarity if 0.6 <= polarity < 0.8:
                        return 'Positive ★★★★★☆'
                  case polarity if 0.8 <= polarity <= 1:
                        return 'Extremely Positive ★★★★★★'
