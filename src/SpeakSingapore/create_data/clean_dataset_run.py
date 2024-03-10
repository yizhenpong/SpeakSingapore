from clean_dataset import CleanDataset

SFP = ["lah", "leh", "lor"]

SinglishERG = CleanDataset(
    "Singlish ERG",
    SFP,
    "data/wikiexamples.txt",
    "cleaned_data/wikiexamples.txt",
    "https://github.com/siewyeng/SinglishERG/blob/main/data/wikidata/wikiexamples.txt",
) # english resource grammar

# SinglishERG.run("[", "]")

NUS_SinglishSMSCorpus = CleanDataset(
    "NUS_SinglishSMSCorpus",
    SFP,
    "data/singlish_corpus.txt",
    "cleaned_data/singlish_corpus.txt",
    "https://www.kaggle.com/datasets/rtatman/the-national-university-of-singapore-sms-corpus",
) 

NUS_SinglishSMSCorpus.run("[", "]")