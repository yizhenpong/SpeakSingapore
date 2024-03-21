'''gpt 4 to normalise sentence and add context'''
from src.SpeakSingapore.clean_data.gpt4_generate_data_main import generateSyntheticData

def get_sentences():
    with open('src/SpeakSingapore/data/Singlish_NUS_SMS/processed_step_2_w_delimiters/singlish_NUS_SMS.txt', 'r') as file:
        lines = file.readlines()
    return lines

def generate_data(lines):
    output_data_path = 'src/SpeakSingapore/data/singlish_NUS_SMS/processed_step_3_gpt4/processed_step_3_gpt4.json'
    generateData = generateSyntheticData(output_data_path, lines)
    generateData.run()

if __name__ == "__main__":
    sentences = get_sentences()
    generate_data(sentences)