# Overview of data sources:

## ICE

## singlish_NUS_SMS
- raw_data: https://www.kaggle.com/datasets/rtatman/the-national-university-of-singapore-sms-corpus
- processed_step_1: extract the sentences from json format, ignore redundant information
- processed_step_2: add delimiters
- processed_step_3: use gpt to normalise sentences (translate to english), while retaining delimiters with SFP and add additional context

## wiki_examples_ERG
- raw_data: https://github.com/siewyeng/SinglishERG/blob/main/data/wikidata/wikiexamples.txt
- processed_step_1: add delimiters