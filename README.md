# SpeakSingapore

### environment
```sh
conda create --name SpeakSingapore
conda activate SpeakSingapore
conda install pip
pip install -r requirements.txt
```

### Lexical tone definitions
To create a common understanding on the various pitch contours of our particles, we established lexical tone definitions, which associate the numerical tone markers with our real-life understanding about the tones of Singlish particles. We adopt a double digit numeric tonal system, spanning from low to high and corresponding to values 1 to 5. Within this framework, the spectrum of tones under examination includes "lah51", "lah21", "lah24", "leh51", "leh21", "leh33", and "lor33".  Our voice recordings for the different pitches are available here: [Lexical Tone Definitions](src/SpeakSingapore/lexical_tone_definitions).

### First ever Singlish Tone dataset!
Building upon these two datasets, we curated the [first ever Singlish tone dataset](src/SpeakSingapore/final_clean_data/aligned_labels_formatted/final_dataset_v2.0.xlsx):
- NUS SMS
    - Chen, Tao, and Min-Yen Kan, "The National University of Singapore SMS Corpus," ScholarBank@NUS Repository, Dataset, March 9, 2015, https://doi.org/10.25540/WVM0-4RNX
- ICE dataset
    - Greenbaum, Sidney, and Gerald Nelson. “The International Corpus of English (ICE) Project.” World Englishes, no. 1 (March 1996): 3–15. https://doi.org/10.1111/j.1467-971x.1996.tb00088.x

All data cleaning scripts are located at [clean_data](src/SpeakSingapore/clean_data) while intermediate processed data are located at [data](src/SpeakSingapore/data)

### Training and Inference
Our training and testing script is available [here](src/SpeakSingapore/test_and_results/training_LLM.ipynb) 
Feel free to use our [model](https://huggingface.co/SinglishToneDetection/Mistral-7B-Instruct-v0.1-speak-singapore-adapter-qLORA) at Huggingface

### Results

Results are available [here](src/SpeakSingapore/test_and_results/result_df_scores.csv) with analysis located [here](src/SpeakSingapore/test_and_results/results_analysis.ipynb)