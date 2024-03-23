'''make json file into csv with following columns
- index, original sentence, new convo by gpt

Clean the conversation MANUALLY such that 
- makes sense
- retains Singlish particles lor lah leh
- add the output label
'''

from src.SpeakSingapore.clean_data.prepare_for_manual_clean import prepareManualClean

original_sentence_file_path =  "src/SpeakSingapore/data/wiki_examples_ERG/processed_step_1_w_delimiters/wikiexamples.txt"
json_input_file_path = "src/SpeakSingapore/data/wiki_examples_ERG/processed_step_2_gpt4/processed_step_2_gpt4.json"
csv_output_file_path = "src/SpeakSingapore/data/wiki_examples_ERG/processed_step_3_manual_clean/processed_step_3_pre_clean.xlsx"
prepare_label = prepareManualClean(original_sentence_file_path, json_input_file_path, csv_output_file_path)
prepare_label.json_to_csv()
