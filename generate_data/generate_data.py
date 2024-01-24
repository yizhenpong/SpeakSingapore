import os
import openai
from openai import OpenAI
  
with open('./generate_data/secrets.txt') as f:
  key = f.readline()
client = OpenAI(api_key=key)

response = client.chat.completions.create(
  model="gpt-4-32k",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)
print(response.choices[0].message.content)