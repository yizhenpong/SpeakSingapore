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
     
        "7 Early, 8 Early (\u4e03\u65e9\u516b\u65e9)": "(Phrase) \u201c7 Early, 8 Early\u201d (\u4e03\u65e9\u516b\u65e9) also common in its hokkien form is used to refer to the time frame between 7am \u2013 8am (or earlier) when some could still be asleep. It is commonly used as a phrase that precedes a complaint of an activity that caused a din disturbing some people who could still be asleep.. Here is a simulated conversation. Ah lian: \u201cEh hello today Sunday leh\u2026.basket I wanna get my beauty sleep lah .. why you 7 early, 8 early bing bing pong pong huh?? sibeh noisy leh\u2026\u2026\n Ah Hua: \u201cPaiseh lah\u2026I meeting my ang moh boyfriend to go jogging mah\u2026.I wanna put makeup first hahah\u2026 Ah lian: \u201cJogging put makeup?? Why don\u2019t you eat and shit at the same time?!?\u201d",
        "5Cs": "(Acronym) 5Cs other than representing the 5 goals of most Singaporeans, it is also the criteria that some females would expect from their future husbands.. Here is a simulated conversation. Cash, Credit Card, Condominium, Car and Country Club Membership are the must haves for some Singaporeans.  Ah Seng: \u201cAh Huay\u2026now of the 5Cs hor, I only have 2 leh\u2026.just a bit of Cash and a Credit Card leh\u2026..will you still be with me till I mati??? Ah Huay:\u00a0\u201cIt\u2019s ok lah, I understand\u2026.no condominium then HDB ok lor, no car we take public transport lor\u2026.no country club membership\u2026.we can go community centre lor Ah Seng:\u00a0\u201cI am so touched\u2026..\u201d *Sob\u2026 Ah Huay:\u00a0\u201cBut\u2026..as long as we are not married and one day if someone who can provide me all these 5Cs and makes me happy suddenly turn up, then don\u2019t blame me hor\u2026\u2026\u2026\u2026..\u201d Ah Seng:\u00a0\u201c\u2026\u2026\u2026\u2026\u2026\u2026\u2026\u2026.\u201d",
        "4D": "(Acronym) 4D is a 4 digit lottery game in Singapore which is run by Singapore Pools.. Here is a simulated conversation. Draws take place on Wednesday, Saturday and Sunday.\n Ah Beng: \u201cAh Lian, if I struck 4D this weekend, I will treat you to eat in an atas restaurant!!",
        "13th Month": "(Noun) 13th Month is a term used to refer to the 13th month bonus which is also known as the Annual Wage Supplement (AWS) that \u201cmost\u201d companies in Singapore give out to permanent staff. This is also known as year-end bonus.. Here is a simulated conversation. Ah Lian: \u201cAh Hua what do you intend to spend on with your\u00a013th Month bonus??? Ah Hua: \u201cAuntie ah, I work as housewife leh, simi 13th Month bonus?? Ah Lian: \u201cYour hubby is your towkay mah, you tell him no money no honey, gimme my money.\u201d",
        "7th Month": "(Noun) This is a festival observed by Singaporean Chinese. The belief is that spirits will emerge when the gates of the netherworld are opened during this period. The Chinese in Singapore will partake in a series of events which include burning of offerings (incense, joss paper, hell notes, paper house, paper car, necessities, etc) for their departed relatives.. Here is a simulated conversation. Some will participate/attend night performances in the form of \u201cGetai\u201d where songs and opera will be performed for both the dead and living. The front row will be kept empty as it is meant for the dead.  Ah Beng: \u201cJohn!!! Be careful!! Don\u2019t step on the offerings on the floor! Now 7th Month!!! John: \u201cAlamak!! Sorry sorry I didn\u2019t mean to step on your offerings, sorry sorry. Let me cross, let me cross\u2026 (\u501f\u8fc7\u3002\u3002\u501f\u8fc7\u3002\u3002) Ah Beng: \u201cWait a minute, John, aren\u2019t you a Christian?? How come you also believe in this?? John: \u201cI am a Chinese after all and it is also a form of respect to other beliefs; and of course it is better to be safe than sorry\u2026.\u201d",
        "10KKJ": "(How it came about) 10KKJ\n. Here is a simulated conversation. 10KKJ is an internet slang that is used to represent Tampines, a town situated in the eastern region of Singapore. It is not commonly used in conversation but frequently used in online forums, text messages and is usually communicated between males. 10KKJ > 10 Ku Ku Jiao > Ten Penis > Tampines Ku Ku Jiao is the hokkien word for penis, so 10KKJ in english is literally \u201cTen-Penis\u201d which phonetically sounds like Tampines.",
        "11B \u2013 Military Identification Card": " 11B is a green Military Identification card issued to Full-Time National Servicemen in Singapore. Compulsory military service is required for every able-bodied Singaporean male aged 18 and above.. Here is a simulated conversation. Upon enlistment, they will surrender their NRIC (National Registration Identity Card) and be issued with the 11B Military Identification card (green) for their stint in National Service. Commonly associated with: ORD, ROD, MR, NRIC, Pink IC \u00a0"
             
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