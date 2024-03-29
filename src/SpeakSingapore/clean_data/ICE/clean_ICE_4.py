import warnings
import os
import re
import glob
import pandas as pd
from h2ogpte import H2OGPTE
from tqdm import tqdm

def run():
    chunked_data_path = os.path.abspath('./src/SpeakSingapore/data/ICE/processed_step_3/ice_data.csv') 
    df = pd.read_csv(chunked_data_path)
    temp = df['0'].apply(lambda x: (re.findall(r"[^\"]\blah|leh|lor\b[^\"]", x)))
    df['num_singlish'] = temp.apply(lambda x: len(x))
    df['output'] = temp
    df.to_csv(chunked_data_path, index=False)

    
if __name__ == "__main__":
    run()