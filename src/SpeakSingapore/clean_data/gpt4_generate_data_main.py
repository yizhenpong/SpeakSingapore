import os
import json
# from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
     
# from langchain.llms import Ollama
# from langchain.callbacks.manager import CallbackManager
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain

class generateSyntheticData():
    def __init__(self, output_data_path, sentences) -> None:
        # self.llm = Ollama(model='mistral',
        #         callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
        with open('src/SpeakSingapore/clean_data/secrets.txt') as f:
            key = f.readline()
        self.llm = OpenAI(openai_api_key=key)
        self.output_data_path = output_data_path
        self.sentences = sentences

    def run(self):
        sentences_to_cache = []
        for sentence_num in range(len(self.sentences)):
            try:
                conversation = self.get_generated_conversation(self.sentences[sentence_num])
                convo_dict = {sentence_num: conversation}
                sentences_to_cache.append(convo_dict)
            except:
                self.cache_conversation(sentences_to_cache)
                sentences_to_cache = []
        self.cache_conversation(sentences_to_cache)
        
    def get_generated_conversation(self, sentence):
        translation_template = """Translate this Singlish sentence with either 'lah, lor, leh'  within square brackets to English text 
                    while retaining 'lah, lor, leh' within square brackets. \n
                    Sentence: '{sentence}' """
        translation_prompt = PromptTemplate(
            input_variables=["sentence"],
            template=translation_template,
        )
        translation_chain = LLMChain(llm=self.llm, prompt=translation_prompt)

        conversation_template = """Craft a brief conversation incorporating the translated Singlish sentence. 
                    Assign each speaker a label (A/B/C) followed by a colon for clarity. 
                    Ensure coherence in the dialogue by providing context and logical flow both before and after the translated Singlish sentence: 
                    '{translated_sentence}' """
        conversation_prompt = PromptTemplate(
            input_variables=["translated_sentence"],
            template=conversation_template,
        )
        conversation_chain = LLMChain(llm=self.llm, prompt=conversation_prompt)
        full_chain = SimpleSequentialChain(chains=[translation_chain, conversation_chain], verbose=True)
        conversation = full_chain.run(sentence)
        return conversation
    
    def cache_conversation(self, sentences_to_cache):
        try:
            with open(self.output_data_path, 'r') as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            existing_data = []
        existing_data.append(sentences_to_cache)
        with open(self.output_data_path, 'w') as f:
            json.dump(existing_data, f, indent=4)

    

if __name__ == "__main__":
    sentences = ['Oh I was thkin of goin yogasana at 10 den no nd to go at 3 den can rush to parco 4 nb Okie [lor] u call me when ready',
                 'Oh I was thkin of goin yogasana at 10 den no nd to go at 3 den can rush to parco 4 nb Okie [lor] u call me when ready', ]
    
    output_data_path = 'src/SpeakSingapore/data/singlish_NUS_SMS/processed_step_3_gpt4/processed_step_3_gpt4.json'
    generateData = generateSyntheticData(output_data_path, sentences)
    generateData.run()