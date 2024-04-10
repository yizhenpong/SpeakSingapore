import pandas as pd
import json
import re

class GenericFormatForCleaning:
    def __init__(self, path, input_col_name, label_col_name, sheetname, stop_at = 999999999):
        df = pd.read_excel(path, sheet_name=sheetname)
        
        for i in range(min(df.shape[0], stop_at)):
            try:
                json.loads(df.loc[i, label_col_name])
            except Exception as e:
                raise Exception(f"loading error on row {i+2} in {df.loc[i, label_col_name]}:\n{e} ") from None
        df[label_col_name] = df[label_col_name].apply(lambda x: json.loads(x))
        self.label_col_name  = label_col_name
        self.input_col_name = input_col_name
        self.df = df

    def replace_text(self, text, particles):
        fin = ""
        for particle in particles:
            text = text.replace(particle[:-2], particle, 1)
            split = text.split(particle)
            fin = fin + split[0] + particle
            try:
                text = split[1]
            except:
                print(text)
                raise Exception("ERROR") from None
            assert len(split) == 2
        return fin

    def run(self, outputcol="output") -> pd.DataFrame:

        self.df[outputcol] = self.df.apply(lambda row: self.replace_text(
            row[self.input_col_name], row[self.label_col_name]
            )
        , axis=1)

        return self.df
    

if __name__ == "__main__":
   
    pd.set_option('display.max_columns', 10)
    format = GenericFormatForCleaning("./src/SpeakSingapore/final_clean_data/aligned_labels/aligned_NUS_SMS_v2.0.xlsx", "conversation", "yz_label", "Sheet1")

    
    out = format.run()
    #print(out)
    out = out[["output", "conversation"]]
    format = GenericFormatForCleaning("./src/SpeakSingapore/final_clean_data/aligned_labels/aligned_NUS_ICE.xlsx", "conversation", "hylabel", "ice_data")
    out_2 = format.run()
    out_2 = out_2[["output", "conversation"]]
    
    out_combined = pd.concat([out, out_2])

    out_combined.to_excel("./src/SpeakSingapore/final_clean_data/aligned_labels_formatted/final_dataset_v2.0.xlsx")
   


           
