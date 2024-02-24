import sys
sys.path.append(r"/Users/pongyizhen/Desktop/Github/SpeakSingapore/src")

from SpeakSingapore.create_data.clean_dataset import CleanDataset

def singlish_SFP_present_test():
    clean_dataset = CleanDataset("Test Dataset", ["lah", "leh", "lor"], "bin/llm_data.json", "bin/testing.txt")
    # Test case with Singlish SFP present
    sentence_with_SFP = "This is a test sentence with lah."
    assert clean_dataset.singlish_SFP_present(sentence_with_SFP) == True
    # Test case without any Singlish SFP
    sentence_without_SFP = "This is a test sentence without any Singlish SFP."
    assert clean_dataset.singlish_SFP_present(sentence_without_SFP) == False


if __name__ == '__main__':
    singlish_SFP_present_test()