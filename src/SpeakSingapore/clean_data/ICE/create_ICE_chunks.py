import chardet
import re
import os
import glob
import pandas as pd
pd.set_option('display.max_columns', None)

def run():
    '''
    create a dataframe of conversation chunks with Singlish particles from ICE-Singapore
    '''
    cleaned_data_path = os.path.abspath('./src/SpeakSingapore/data/ICE/processed_step_1/') 
    dump_path = os.path.abspath('./src/SpeakSingapore/data/ICE/processed_step_2') 
    csv_files = glob.glob(os.path.join(cleaned_data_path, '*.csv'))
    
    for csv in csv_files:
        df = pd.read_csv(csv)
        
        df['speakerlag3'] = df.speaker.shift(3)
        df['speechlag3'] = df.speech.shift(3)

        df['speakerlag2'] = df.speaker.shift(2)
        df['speechlag2'] = df.speech.shift(2)

        df['speakerlag'] = df.speaker.shift(1)
        df['speechlag'] = df.speech.shift(1)

        df['speakerlead'] = df.speaker.shift(-1)
        df['speechlead'] = df.speech.shift(-1)

        df['speakerlead2'] = df.speaker.shift(-2)
        df['speechlead2'] = df.speech.shift(-2)

        df['speakerlead3'] = df.speaker.shift(-3)
        df['speechlead3'] = df.speech.shift(-3)
        
        


        break

if __name__ == "__main__":
    run()
