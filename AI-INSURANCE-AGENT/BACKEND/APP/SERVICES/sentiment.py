import openai
import analyze_sentiment, get_sentiment_message
from app.services.sentiment import analyze_sentiment, get_sentiment_message

async def generate_response(query: str, user_profile: dict = None):
    sentiment = analyze_sentiment(query)
    sentiment_msg = get_sentiment_message(sentiment)

    context = f"User Profile: {user_profile}" if user_profile else ""
    prompt = f"{context}\nUser sentiment: {sentiment}\n{sentiment_msg}\nAnswer this insurance query: {query}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an empathetic insurance advisor."},
            {"role": "user", "content": prompt}
        ]
    )

    return response["choices"][0]["message"]["content"]
