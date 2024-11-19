from modules.stm_analyzer import StmAnalyzer
from interface.interface_layout import layout

def app():
      analyzer = StmAnalyzer()
      try:
            # app layout
            layout()
            # user input for text analysis
            text = str(input("Enter a text to analyze its sentiment: "))
            # analyze sentiment and print result
            sentiment = analyzer.analyze_sentiment(text)
            print(f"The sentiment of the given text is: {sentiment}")
      except KeyboardInterrupt:
            print("Program interrupted by user.")
      except Exception as e:
            print(f"An error occurred: {str(e)}")

if "__main__" == __name__:
      app()