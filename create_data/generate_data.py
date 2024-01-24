import os
import openai
import json
from openai import OpenAI
from utils import write_to_json_file
  
with open('./create_data/secrets.txt') as f:
  key = f.readline()
client = OpenAI(api_key=key)

response = client.chat.completions.create(
  model="gpt-4-1106-preview",
  response_format={"type": "json_object" },
  messages=[
    {"role": "system", "content": 
    """You are a helpful assistant who is  designed to help finetune a large language model.
    All of your outputs must be in JSON.
    """},
    {"role": "user", "content": """
im trying to format a dataset to fine-tune my large language model. My prompt is formatted as such:
 {
        "role": "system",
        "content": "You are a friendly chatbot who is knowledgeable about Singapore and its culture",
    },
    {
        "role": "user",
     "content": "walao eh"
     },
{
 "role": "assistant",
"content":  "Walao eh is used mostly to express disapproval, but can also be used to show one's disbelief, ie. a surprise. For example, when visiting a durian stall, one may say 'Walao-eh! This durian so big sia!' "
}

     This is one example. Please generate me many more examples, which focus on explaining common Singlish phrases. Please append all of these json objects together in a single JSON list. To help you, please refer to these Singlish phrases and their definitions.
     
    
        "Atas": "Atas Origin: Malay\u00a0\u2013 a term to describe\u00a0a person or some place that is high class Atas can be used to describe someone as being arrogant or snobbish but is more commonly used now to describe someone doing things that is high class and of good taste.",
        "Abang": "Abang Origin: Malay \u2013 the term for elder brother and is also informally used to address a malay friend. Abang is a malay term for elder brother or just simply brother. It is common to call a male malay friend \u201cabang\u201d as it is akin to calling him \u201cHi Bro\u201d.",
        "Ah Huay": "Ah Huay Origin:\u00a0Hokkien,\u00a0Ah Huay is the hokkien pronunciation of the chinese name \u963f\u82b1",
        "Ah Lian": "Ah Lian Origin:\u00a0Hokkien,\u00a0Ah Lian is the hokkien pronunciation of the chinese name \u963f\u83b2.",
        "Ah Seng": "Ah Seng Origin: Hokkien,\u00a0Ah Seng is the hokkien pronunciation of the chinese name \u963f\u9648.",
        "agar-agar": "agar-agar Origin: Malay \u2013\u00a0\u00a0a dessert that is similar to jelly. agar-agar is a jelly-like dessert derived from algae. It can also be used as an ingredient to complement other desserts. agar-agar itself can also be added with fruit slices or coconut milk to enhance its taste and appearance.",
        "Alamak": "Alamak Origin: Malay \u2013 An exclamation word\u00a0to express shock or\u00a0surprise Alamak is an exclamation word used in situations when you are shocked or surprised by something or an event. It is something akin to \u201cOh my Mother!\u201d and also \u201cOh my God!\u201d.",
        "Ang Moh": "Ang Moh Origin: Hokkien \u2013 It literally means \u201cRed hair\u201d but is used as a term to represent Caucasians Ang Moh is a term that is used to refer to Caucasians. In the past, older people who disliked Caucasians will call them \u201cAng Moh Gui\u201d (\u7ea2\u6bdb\u9b3c) which literally means \u201cred hair ghost\u201d.",
        "AWARE \u2013 Association of Women for Action and Research": "AWARE Origin: Acronym/English \u2013 stands for Association of Women for Action and Research AWARE is a non-governmental organization in Singapore that is involved in research and advocacy for women and to promote gender equality.",
        "Agak, Agak-Agak, Agaration": "Agak, Agak-Agak, Agaration Origin: Malay \u2013 agak means to estimate Agak and agak-agak are both malay words and are used to describe to estimate/guess. It is a conjecture usually based on one\u2019s experience or one\u2019s estimation."
        
     Here is what your output should be like, but please generate more examples:
[
[
{
        "role": "system",
        "content": "You are a friendly chatbot who is knowledgeable about Singapore and its culture",
    },
    {
        "role": "user",
     "content": "what does walao eh mean in Singlish"
     },
{
 "role": "assistant",
"content":  "Walao eh is used mostly to express disapproval, but can also be used to show one's disbelief, ie. a surprise. For example, when visiting a durian stall, one may say 'Walao-eh! This durian so big sia!' "
}
],
[
{
    "role": "system",
    "content": "You are a friendly chatbot who is knowledgeable about Singapore and its culture"
},
{
    "role": "user",
    "content": "I need help understanding this Singlish passage: 'Wah, that movie damn chim sia. Watch until my brain pain. Confirm director tok kong one. After that, go makan with friends, sibei shiok! Got try the new dessert shop, damn power.'"
},
{
    "role": "assistant",
    "content": "Certainly! Here's the translation: 'Wow, that movie is really intellectual. Watching it gave me a headache. The director is definitely top-notch. After that, I went to eat with friends, and it was extremely enjoyable! We tried the new dessert shop, and it was amazing.'"
}

]

]
     """     
     }
  ]
)
print(response.choices[0].message.content)
write_to_json_file('data/llm_data.json', response.choices[0].message.content, string=True)