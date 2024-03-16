import warnings
import os
import re
import glob
import pandas as pd


def run():
    chunked_data_path = os.path.abspath('./src/SpeakSingapore/data/ICE/processed_step_2/') 
    ls = list(
        pd.read_csv(
            chunked_data_path + "/convs.csv", index_col=None
            )['0']
        )
    final_series = pd.Series(list(map(format_prompt, ls)))
    final_series.to_csv(os.path.abspath('./src/SpeakSingapore/data/ICE/processed_step_3/ice_data.csv') )
    


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