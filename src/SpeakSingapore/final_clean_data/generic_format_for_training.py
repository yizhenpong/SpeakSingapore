import pandas as pd
import json
import re

class GenericFormatForCleaning:
    def __init__(self, path, input_col_name, label_col_name, sheetname):
        df = pd.read_excel(path, sheet_name=sheetname)
        for i in range(df.shape[0]):
            try:
                json.loads(df.loc[i, label_col_name])
            except Exception as e:
                raise Exception(f"loading error on row {i+2} in {df.loc[i, label_col_name]}:\n{e} ") from None
        df[label_col_name] = df[label_col_name].apply(lambda x: json.loads(x))
        self.label_col_name  = label_col_name
        self.input_col_name = input_col_name
        self.df = df

    def replace_text(self, text, particles):
        for particle in particles:
            text = text.replace(particle[:-2], particle, 1)
        return text

    def run(self) -> pd.DataFrame:
        self.df[self.label_col_name] = self.df.apply(lambda row: self.replace_text(
            row[self.input_col_name], row[self.label_col_name]
            )
        , axis=1)
        return self.df
    

if __name__ == "__main__":
    import os
    print(os.getcwd()) 
    format = GenericFormatForCleaning("./src/SpeakSingapore/final_clean_data/aligned_labels/aligned_NUS_SMS.xlsx", "conversation", "output", "Sheet1")

    pd.set_option('display.max_columns', 10)
    out = format.run()
    print(out)
    out.to_excel("./src/SpeakSingapore/final_clean_data/aligned_labels_with_source/final_dataset.xlsx")
   # print(format.run().to_csv("./src/SpeakSingapore/clean_data/test_generic_format_data/output.csv"))


           
