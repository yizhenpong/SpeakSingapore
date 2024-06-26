'''clean dataset module
be careful when u rerun this for the same dataset 
as module is formatted to append to the text file clean_data_path
and there is extra sentence "====== end of run ======" at the end
'''
import pathlib
import re

class AbstractCleanDataset:
    '''Abstract class'''
    def __init__(self, name: str, SFP: list, data_path: pathlib.Path, clean_data_path: pathlib.Path, source: str) -> None:
        '''initialise with dataset name and a list of sentence final particles to be identified'''
        self.name = name
        self.SFP = SFP
        self.data_path = data_path
        self.clean_data_path = clean_data_path
        self.source = source
    
    def singlish_SFP_present(self, sentence: str) -> bool:
        '''Check if Singlish Sentence Final Particle is present in sentence'''
        raise NotImplementedError
    
    def put_singlish_particle_within_delimiter(self, sentence: str, delimiter: str):
        '''Place Singlish words within delimiters'''
        raise NotImplementedError
    
    def save_sentence_to_file(self, sentence: str):
        '''Save sentence to file'''
        raise NotImplementedError

class CleanDataset(AbstractCleanDataset):
    '''Clean dataset -- generic'''
    def singlish_SFP_present(self, sentence: str) -> bool:
        '''check if singlish SFP in sentence'''
        punctuation_pattern = r'[^\w\s]'
        cleaned_sentence = re.sub(punctuation_pattern, '', sentence)
        sfp_set = set(self.SFP)
        for word in cleaned_sentence.split():
            if word.lower() in sfp_set:
                return True
        return False
    
    def put_singlish_particle_within_delimiter(self, sentence: str, start_delimiter: str, end_delimiter: str) -> str:
        '''Place Singlish words within specified delimiters'''
        punctuation_pattern = r'[^\w\s]'
        cleaned_sentence = re.sub(punctuation_pattern, '', sentence)
        if self.singlish_SFP_present(cleaned_sentence):
            words = cleaned_sentence.split()
            for i, word in enumerate(words):
                if word.lower() in self.SFP:
                    words[i] = f"{start_delimiter}{word}{end_delimiter}"
            return ' '.join(words)
        else:
            return ''
    
    def save_sentence_to_file(self, sentence: str):
        '''Save sentence to file'''
        with open(self.clean_data_path, 'a', encoding='utf-8') as file:
            file.write(sentence + '\n')
    
    def run(self, start_delimiter, end_delimiter):
        with open(self.data_path, 'r', encoding='utf-8') as file:
            for sentence in file:
                new_sentence = self.put_singlish_particle_within_delimiter(sentence, start_delimiter, end_delimiter)
                if new_sentence != '':
                    self.save_sentence_to_file(new_sentence)
        self.save_sentence_to_file("====== end of run ======")
        print(f"saved all cleaned sentence into {self.clean_data_path}")

