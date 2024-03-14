from src.SpeakSingapore.clean_data.clean_dataset_main import CleanDataset

SFP = ["lah", "leh", "lor"]

SinglishERG = CleanDataset(
    "Singlish ERG",
    SFP,
    "src/SpeakSingapore/data/wiki_examples_ERG/raw_data/wikiexamples.txt",
    "src/SpeakSingapore/data/wiki_examples_ERG/processed_step_1_w_delimiters/wikiexamples.txt",
    "https://github.com/siewyeng/SinglishERG/blob/main/data/wikidata/wikiexamples.txt",
) # english resource grammar

if __name__ == "__main__":
    SinglishERG.run("[", "]")