import warnings
import os
import re
import glob
import pandas as pd
from h2ogpte import H2OGPTE
from tqdm import tqdm

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
    chunked_data_path = os.path.abspath('./src/SpeakSingapore/data/ICE/processed_step_2/') 
    ls = list(
        pd.read_csv(
            chunked_data_path + "/convs.csv", index_col=None
            )['0']
        )
    
    client = load_llm()
    
    for i in tqdm(range(len(ls))):

        output = answer(
            client,
            "The following is a conversation between one or more people, in Singlish, directly transcribed. \
                Clean up the text as much as possible, converting it into proper Singlish text. \
                    Ensure that your output is still in Singlish and retains its original syntax.\
                         Below is an example. Note that in the example, the cleaned output adds punctuation, removes duplicate words.\nA: So you you try to call as many as possible lor see how\nYour cleaned output should be:\nA: So you try to call as many as possible lor, see how.\n\
                            Now, with the example in mind, clean the following conversation below.\n"\
                              + ls[i]

            ).content
        
        ls[i] = output
        if i%100 == 0:
            # Store backup
            partial_series = pd.Series(list(map(format_prompt, ls)))
            partial_series.to_csv(os.path.abspath('./src/SpeakSingapore/data/ICE/processed_step_3/ice_data.csv'), index=False)

       

    final_series = pd.Series(list(map(format_prompt, ls)))
    final_series.to_csv(os.path.abspath('./src/SpeakSingapore/data/ICE/processed_step_3/ice_data.csv'), index=False)
    '''
    Manual edits follow this.
    '''


def format_prompt(convo):
    formatted = [
        {
            "role" : "user",
            "content":  """Below is a transcript of a conversation involving Singaporeans who are speaking Singlish. Singlish is an English-based creole and contains particles such as "lah", "lor" and "leh". These particles have different pitches, depending on the context of the conversation. For the provided conversation transcript, attach an appropriate pitch for the Singlish particles:\n""" + convo
        }
    ]
    return formatted

if __name__ == "__main__":
    run()