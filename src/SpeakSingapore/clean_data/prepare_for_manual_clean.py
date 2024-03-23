import json
import openpyxl
import pandas as pd

class prepareManualClean():
    def __init__(self, original_sentence_file_path, 
                json_input_file_path, 
                csv_output_file_path) -> None:
        self.original_sentence_file_path = original_sentence_file_path
        self.json_input_file_path = json_input_file_path
        self.csv_output_file_path = csv_output_file_path

    def json_to_csv(self):
        with open(self.json_input_file_path, 'r') as file:
            data = json.load(file)
            data = data[0]
        with open(self.original_sentence_file_path, 'r') as file:
            lines = file.readlines()
        combined_data = pd.DataFrame(columns=['original_sentence', 'conversation'])
        for i in range(len(data)-1):
            row_data = {'original_sentence': lines[i], 'conversation': data[i][str(i)]}
            row_data = pd.DataFrame(row_data, index=[0])
            combined_data = pd.concat([combined_data,row_data], ignore_index=True)
        with pd.ExcelWriter(self.csv_output_file_path, engine='xlsxwriter') as writer:
            combined_data.to_excel(writer, index=False, sheet_name='singlish_NUS_SMS')
            workbook = writer.book
            worksheet = writer.sheets['singlish_NUS_SMS']
            format_wrap = workbook.add_format({'text_wrap': True})
            worksheet.set_column('A:B', width=50, cell_format=format_wrap)




    



