from clean_dataset import CleanDataset

SinglishERG = CleanDataset(
    "Singlish ERG",
    ["lah", "leh", "lor"],
    "data/wikiexamples.txt",
    "cleaned_data/wikiexamples.txt",
    "https://github.com/siewyeng/SinglishERG/blob/main/data/wikidata/wikiexamples.txt",
) # english resource grammar

SinglishERG.run("[", "]")