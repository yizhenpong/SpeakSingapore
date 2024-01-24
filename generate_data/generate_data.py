import os
import openai
from openai import OpenAI
    
openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4 turbo",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)
print(response.choices[0].message.content)