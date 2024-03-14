import chardet
import re
import os
import glob
import numpy as np
import pandas as pd

def run():
    '''
    clean data from ICE-Singapore
    '''
    
    cleaned_data_path = os.path.abspath('./src/SpeakSingapore/data/ICE/processed_step_1/{name}.csv') 
    
    ice_path = os.path.abspath('./src/SpeakSingapore/data/ICE/raw_data') 
    txt_files = glob.glob(os.path.join(ice_path, 'S1*.txt'))
   
    i = 1
    for txt_file in txt_files:
    # Open the file and read its content
        print(txt_file)
        convo = []
        
        with open(txt_file, 'r', encoding=detect_encoding(txt_file)) as file:
            curr_speaker = np.NaN
            curr_speech = []
            for line in file:
                if re.match(r"^<ICE-SIN.*>", line):
                    chunk = (curr_speaker, ' '.join(curr_speech))
                    convo.append(chunk)
                    curr_speaker = line[-3:-2]
                    curr_speech = []
                    
                elif not re.match(r"^<[\$I].*>", line) and line.rstrip():
                   
                    pattern = r"<[Oo\&]>[ ](.*?)[ ]</[Oo\&]>" # all <O> </O> or <&> etc. are converted to * *.
                    to_replace = r"*\1*"
                    mline = re.sub(pattern, to_replace, line.rstrip())
                    curr_speech.append(mline)

            chunk = (curr_speaker, ' '.join(curr_speech))
            convo.append(chunk)
            convo = convo[1:] # omit first line
       
        speakers, speeches = zip(*convo)
        df = pd.DataFrame({
            'speaker': speakers,
            'speech': speeches
        })

   
        df.to_csv(cleaned_data_path.format(name=f"ICE-{str(i)}"), index=False)
        i+=1


    
def detect_encoding(path):
    with open(path, 'rb') as raw:
        result = chardet.detect(raw.read())
        encoding = result['encoding']
    return encoding
    
   

def write_to_file(path, content):
    f = open(path, 'w')
    f.write(content)
    f.close()


if __name__ == "__main__":
    run()