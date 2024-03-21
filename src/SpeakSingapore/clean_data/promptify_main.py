'''promptify conversation module
Format dataset such that it is suitable to be used as data to train an LLM model
- Input data will be in csv format with the following columns
    - index, conversation, num_singlish_particles, output
- place the conversation in the {role, content format} 
    - index, formatted conversation w output
'''
import pathlib
import json
import pandas as pd

class Promptify_Convo:
    def __init__(self, input_csv_path: pathlib.Path, output_json_path: pathlib.Path) -> None:
        self.input_csv_path = input_csv_path
        self.output_json_path = output_json_path
    
    def run_promptify(self):
        df = pd.read_csv(self.input_csv_path)
        dataset = []
        for row_num in range(len(df)):
            row = df.iloc[row_num]
            print(row['conversation'])
            print(row['num_singlish_particles'])
            print(row['output'])
            formatted = \
                self._format_conversation(row['conversation'], row['num_singlish_particles'], row['output'])
            dataset_row = {"id": row_num, "conversations": formatted}
            dataset.append(dataset_row)
        with open(output_json_path, "w") as json_file:
            json.dump(dataset, json_file, indent=4)

    def _format_conversation(self, conversation_utterances, num_particles, output):
        law_of_Singlish_pitches = ""
        standard_user_template = \
            f"""Below is a transcript of a conversation involving Singaporeans who are speaking Singlish. 
                Singlish is an English-based creole and contains particles such as "lah", "lor" and "leh". 
                These particles have different pitches, depending on the context of the conversation. 

                Here is the comprehensive law of Singlish pitches you must remember and follow when labeling the pitch: \n
                {law_of_Singlish_pitches}

                For the provided conversation transcript, there is a total of {num_particles} Singlish particles,
                attach an appropriate pitch for the Singlish particles:\n"""
        standard_llm_tempate = f"Here is the conversation with labeled Singlish pitches: {output}"

        formatted = [
            {
                "role" : "user",
                "content":  standard_user_template + conversation_utterances
            },
            {
                "role" : "bot",
                "content": standard_llm_tempate
            }
        ]
        return formatted
    
if __name__ == "__main__":
    input_csv_path = "src/SpeakSingapore/data/test_promptify_data.csv"
    output_json_path  = "src/SpeakSingapore/data/test_promptify_data_output.json"
    promtify = Promptify_Convo(input_csv_path, output_json_path)
    promtify.run_promptify()

    
        