from clean_dataset import CleanDataset

SFP = ["lah", "leh", "lor"]

NUS_SinglishSMSCorpus = CleanDataset(
    "NUS_SinglishSMSCorpus",
    SFP,
    "data/singlish_corpus.txt",
    "processed_data_step_1/singlish_corpus.txt",
    "https://www.kaggle.com/datasets/rtatman/the-national-university-of-singapore-sms-corpus",
) 

# NUS_SinglishSMSCorpus.run("[", "]")