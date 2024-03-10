'''
From the following sources, extract the relevant Singlish keywords, return json file 

{
    'singlish word 1 (lower)': explanation
    'singlish word 2 (lower)': explanation
    ...
}

Source: 
https://www.singlish.net/category/dictionary/numeric/
https://www.singlish.net/category/dictionary/a/
...
https://www.singlish.net/category/dictionary/z/
'''
import os
import requests
from bs4 import BeautifulSoup
from utils import write_to_json_file

all_singlish_words = {}
# def get_page_content(URL):

# To bypass 403 forbidden error
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
BASE_URL = 'https://www.singlish.net/'
URL = BASE_URL + 'category/dictionary/'
PAGES = ['numeric'] + [chr(i) for i in range(97, 97+26)]
for curr in PAGES:
    
    curr_page = curr
    url_curr = URL + curr_page

    page = requests.get(url_curr, headers=HEADERS)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="content") #div id = content
    # print(results.prettify())

    keywords = results.find_all("h2", class_="entry-title")
    keywords_explanations = results.find_all("div", class_="entry-content")
    i = 0
    all_words_in_cat = {}
    for keyword in keywords:
        singlish_word = keyword.a.get_text() #keyword looks like this: <h2 class="entry-title"><a href="https://www.singlish.net/5cs/" rel="bookmark">5Cs</a></h2>
        
        #print(keyword.a.get("href"))
        word_url = keyword.a.get("href")
        
        word_page = requests.get(word_url, headers=HEADERS)
        soup_page = BeautifulSoup(word_page.content, "html.parser")
        
        results_page = soup_page.find(id="content") 
        print(singlish_word)
        try:
            type_of_word = f"({results_page.find_all('h4')[1].get_text(strip=True)}"[:-1] + ")" # Obtain type of word.
            # remove : symbol
        except:
            type_of_word = ""
       
        definition = list(map(lambda x: x.get_text(strip=False), results_page.find_all('p')))[:-10]
        explanation = f"{type_of_word} {definition[0]}. Here is a simulated conversation. {' '.join(definition[1:])}"
       
        all_words_in_cat[singlish_word] = explanation
        i+=1
   
    all_singlish_words[curr_page] = all_words_in_cat
    # print(all_singlish_words)
    write_to_json_file('data/singlish_words.json', all_singlish_words)


