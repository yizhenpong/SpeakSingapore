from src.SpeakSingapore.clean_data.clean_dataset_main import CleanDataset

SFP = ["lah", "leh", "lor"]

NUS_SinglishSMSCorpus = CleanDataset(
    "NUS_SinglishSMSCorpus",
    SFP,
    "data/processed_step_1/singlish_corpus.txt",
    "data/processed_step_2_w_delimiters/singlish_corpus.txt",
    "https://www.kaggle.com/datasets/rtatman/the-national-university-of-singapore-sms-corpus",
) 

if __name__ == "__main__":
    NUS_SinglishSMSCorpus.run("[", "]")