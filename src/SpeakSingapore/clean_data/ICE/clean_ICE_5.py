import warnings
import os
import re
from h2ogpte import H2OGPTE
from tqdm import tqdm

import pandas as pd
pd.set_option('display.max_columns', None)


def load_llm():
    with open('./create_data/secrets.txt') as f:
        api = f.read()
        
    client = H2OGPTE(
    address="https://h2ogpte.genai.h2o.ai",
    api_key=api
    )
 
    return client

def answer(client, userquery, sysprompt= "You are a helpful assistant who helps the user with their tasks.", llm='mistralai/Mixtral-8x7B-Instruct-v0.1'):
    return client.answer_question(
        question = userquery,
        system_prompt = sysprompt,
        llm=llm
    )

def run():
    SYSPROMPT = '''
    You will be provided a conversation between one or more people in Singlish by the user. Make use of the information provided to you below.
    Singlish is an English-based creole and is widely known for its particles, lah, leh, and lor. 
    Each particle may have 1 or more tone contours, which affects the meaning and tone of the sentence.
    
    The particle lah has 3 tones, lah²¹ (low tone), lah²⁴ (rising tone) and lah⁵¹.
    lah²¹ is indicative of more matter-of-factness, lah²⁴ is indicative of persuasiveness. 
    For example, if someone says "I'm tired lah²⁴", they would likely be trying to be persuasive. For example, they are trying to convince someone that they do not want to go out.

    lah⁵¹, on the other hand, often indicates that one is aware about something and would like to share/confirm it, akin to "I already know".
    For example, if someone informs you that they had broken a leg, you would deduce that they cannot walk and say "So you cannot walk lah⁵¹"
    
    '''
    path =  os.path.abspath('./src/SpeakSingapore/data/ICE/processed_step_2/convs.csv')
    df = pd.read_csv(path)
    client = load_llm()
    #answer(client, "hi")
    for i in range(len(df['0'])):
        print(df['0'][i])
        break

if __name__ == "__main__":
    run()