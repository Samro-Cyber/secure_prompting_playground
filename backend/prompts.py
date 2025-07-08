import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

SYSTEM_PROMPT = "You are a helpful assistant."

def sanitize_input(user_input):
    return user_input.replace("ignore previous", "").replace("\n", " ")

def get_response_with_filter(user_input, apply_filter=False):
    prompt = sanitize_input(user_input) if apply_filter else user_input
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content.strip()
