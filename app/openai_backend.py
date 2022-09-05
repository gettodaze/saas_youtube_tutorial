import os
import openai

from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
response = openai.Completion.create(
    model="text-davinci-002", prompt="Say this is a test", max_tokens=6, temperature=0
)

print(response)
