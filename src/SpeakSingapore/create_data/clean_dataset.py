'''clean dataset module'''

class AbstractCleanDataset:
    def __init__(self, name: str, SFP: list) -> None:
        self.name = name
        self.SFP = SFP
    
    def singlish_SFP_present(self, sentence: str) -> bool:
        '''Check if Singlish Sentence Final Particle is present in sentence'''
        raise NotImplementedError
    
    def put_singlish_particle_within_delimiter(self, sentence: str, delimiter: str):
        '''Place Singlish words within delimiters'''
        raise NotImplementedError
    

class CleanDataset(AbstractCleanDataset):
    def __init__(self, name: str, SFP: list) -> None:
        '''initialise with dataset name and a list of sentence final particles to be identified'''
        super().__init__(name, SFP)

    def singlish_SFP_present(self, sentence: str) -> bool:
        '''check if singlish SFP in sentence'''
        sfp_set = set(self.SFP)
        for word in sentence.split():
            if word.lower() in sfp_set:
                return True
        return False
    
    def put_singlish_particle_within_delimiter(self, sentence: str, start_delimiter: str, end_delimiter: str) -> str:
        '''Place Singlish words within specified delimiters'''
        if self.singlish_SFP_present(sentence):
            words = sentence.split()
            for i, word in enumerate(words):
                if word.lower() in self.SFP:
                    words[i] = f"{start_delimiter}{word}{end_delimiter}"
            return ' '.join(words)
        else:
            return sentence