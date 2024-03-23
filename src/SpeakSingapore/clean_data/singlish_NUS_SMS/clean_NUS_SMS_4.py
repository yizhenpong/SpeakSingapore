'''make json file into csv with following columns
- index, original sentence, new convo by gpt

Clean the conversation MANUALLY such that 
- makes sense
- retains Singlish particles lor lah leh
- add the output label
'''

from src.SpeakSingapore.clean_data.prepare_for_manual_label import prepareManualLabel

original_sentence_file_path =  "src/SpeakSingapore/data/singlish_NUS_SMS/processed_step_2_w_delimiters/singlish_NUS_SMS.txt"
json_input_file_path = "src/SpeakSingapore/data/singlish_NUS_SMS/processed_step_3_gpt4/processed_step_3_gpt4.json"
csv_output_file_path = "src/SpeakSingapore/data/singlish_NUS_SMS/processed_step_4_manual_label/processed_step_4_to_label.xlsx"
prepare_label = prepareManualLabel(original_sentence_file_path, json_input_file_path, csv_output_file_path)
prepare_label.json_to_csv()
