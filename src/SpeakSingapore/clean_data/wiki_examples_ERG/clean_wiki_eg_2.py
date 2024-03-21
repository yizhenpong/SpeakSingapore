'''gpt 4 to normalise sentence and add context'''
from src.SpeakSingapore.clean_data.gpt4_generate_data_main import generateSyntheticData

def get_sentences():
    with open('src/SpeakSingapore/data/wiki_examples_ERG/processed_step_1_w_delimiters/wikiexamples.txt', 'r') as file:
        lines = file.readlines()
    return lines

def generate_data(lines):
    output_data_path = 'src/SpeakSingapore/data/wiki_examples_ERG/processed_step_2_gpt4/processed_step_2_gpt4.json'
    generateData = generateSyntheticData(output_data_path, lines)
    generateData.run()

if __name__ == "__main__":
    sentences = get_sentences()
    generate_data(sentences)