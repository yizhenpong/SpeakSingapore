'''add delimiters to sentences'''
from src.SpeakSingapore.clean_data.clean_dataset_main import CleanDataset

SFP = ["lah", "leh", "lor"]

NUS_SinglishSMSCorpus = CleanDataset(
    "NUS_SinglishSMSCorpus",
    SFP,
    "src/SpeakSingapore/data/Singlish_NUS_SMS/processed_step_1/singlish_NUS_SMS.txt",
    "src/SpeakSingapore/data/Singlish_NUS_SMS/processed_step_2_w_delimiters/singlish_NUS_SMS.txt",
    "https://www.kaggle.com/datasets/rtatman/the-national-university-of-singapore-sms-corpus",
) 

if __name__ == "__main__":
    NUS_SinglishSMSCorpus.run("[", "]")