
import warnings
import os
import re
import glob
import pandas as pd
pd.set_option('display.max_columns', None)

def run():
    '''
    create a dataframe of conversation chunks with Singlish particles from ICE-Singapore
    '''
    cleaned_data_path = os.path.abspath('./src/SpeakSingapore/data/ICE/processed_step_1/') 
    dump_path = os.path.abspath('./src/SpeakSingapore/data/ICE/processed_step_2/') 
    csv_files = glob.glob(os.path.join(cleaned_data_path, '*.csv'))

    conv_to_csv = []
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
        df = df.fillna("")

        # reorder
        LIST_OF_PARTICLES = ['lah', 'lor', 'meh', 'ah', 'la']
        pattern = r"\b" + "|".join(LIST_OF_PARTICLES) + r"\b"
        with warnings.catch_warnings():
            warnings.simplefilter(action='ignore')
            filtered = df[df['speech'].str.contains(pattern, case=False)]
            # focus on the particle filtered in the middle sentence.
            filtered.speech = filtered.speech.map(lambda x: re.sub(r'\b(lah|lor|meh|ah|la)\b', r"[\1]", x))
            
        filtered = filtered[list(filtered.columns)[2:8] + list(filtered.columns)[0:2] + list(filtered.columns)[8:]]
       
        
        for _, row in filtered.iterrows():
            tmp = row.tolist()
            filtered_conv ='\n'.join(
                [f"{tmp[i]}: {tmp[i+1]}" for i in range(0, len(tmp)-1, 2) if tmp[i] and tmp[i+1]]
            )

            conv_to_csv.append(filtered_conv)
            

    series = pd.Series(conv_to_csv)
    series.to_csv(dump_path + '/convs.csv')

if __name__ == "__main__":
    run()
