from textblob import TextBlob

def analyze_sentiment(text: str) -> str:
    """
    Analyze the sentiment of the given text and return:
    - 'Positive' for positive sentiment
    - 'Negative' for negative sentiment
    - 'Neutral' for neutral sentiment
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Polarity score ranges from -1.0 to 1.0

    if polarity > 0.2:
        return "Positive"
    elif polarity < -0.2:
        return "Negative"
    else:
        return "Neutral"


def get_sentiment_message(sentiment: str) -> str:
    """
    Return an empathetic message based on the detected sentiment.
    """
    if sentiment == "Positive":
        return "Great! I can help you explore more options."
    elif sentiment == "Negative":
        return "I understand your concern. Let me simplify this for you."
    else:
        return "Sure, let's look at your options together."
