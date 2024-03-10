import sys
sys.path.append(r"/Users/pongyizhen/Desktop/Github/SpeakSingapore/src")

from SpeakSingapore.create_data.clean_dataset import CleanDataset

def singlish_SFP_present_test():
    clean_dataset = CleanDataset("Test Dataset", ["lah", "leh", "lor"], "recycle_bin/llm_data.json", "recycle_bin/testing.txt", "temporary source")
    # Test case with Singlish SFP present
    sentence_with_SFP = "This is a test sentence with lah"
    assert clean_dataset.singlish_SFP_present(sentence_with_SFP) == True
    sentence_with_SFP_punc = "This is a test sentence with lah."
    assert clean_dataset.singlish_SFP_present(sentence_with_SFP_punc) == True
    # Test case without any Singlish SFP
    sentence_without_SFP = "This is a test sentence without any Singlish SFP."
    assert clean_dataset.singlish_SFP_present(sentence_without_SFP) == False

def put_singlish_particle_within_delimiter_test():
    clean_dataset = CleanDataset("Test Dataset", ["lah", "leh", "lor"], "recycle_bin/llm_data.json", "recycle_bin/testing.txt", "temporary source")
    sentence_with_SFP = "This is a test sentence with lah"
    assert clean_dataset.put_singlish_particle_within_delimiter(sentence_with_SFP, "[", "]") == "This is a test sentence with [lah]"

def save_sentence_to_file_test():
    clean_dataset = CleanDataset("Test Dataset", ["lah", "leh", "lor"], "recycle_bin/llm_data.json", "recycle_bin/testing.txt", "temporary source")
    sentence_with_SFP = "This is a test sentence with lah"
    clean_dataset.save_sentence_to_file(sentence_with_SFP)


if __name__ == '__main__':
    singlish_SFP_present_test()
    put_singlish_particle_within_delimiter_test()
    save_sentence_to_file_test()
    save_sentence_to_file_test()