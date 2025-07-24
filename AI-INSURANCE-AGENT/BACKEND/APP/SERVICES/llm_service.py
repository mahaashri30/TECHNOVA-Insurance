import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_response(query: str, user_profile: dict = None):
    # Add context about user profile
    context = f"User Profile: {user_profile}" if user_profile else ""
    prompt = f"{context}\nAnswer this insurance query: {query}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an insurance advisor."},
                  {"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
