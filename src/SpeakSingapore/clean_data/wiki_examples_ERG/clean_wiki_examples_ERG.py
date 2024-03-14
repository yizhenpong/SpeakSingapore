from SpeakSingapore.clean_data.clean_dataset_main import CleanDataset

SFP = ["lah", "leh", "lor"]

SinglishERG = CleanDataset(
    "Singlish ERG",
    SFP,
    "data/wikiexamples.txt",
    "processed_data_step_1/wikiexamples.txt",
    "https://github.com/siewyeng/SinglishERG/blob/main/data/wikidata/wikiexamples.txt",
) # english resource grammar

# SinglishERG.run("[", "]")