import requests, json
import pandas as pd
import numpy as np
from collections import Counter
import os
import re
import string
string.punctuation

def getUniqueWords(phrase): 
    '''
    Takes a string phrase, create the vocabulary of unique words.
    '''
    textchunk = phrase.lower()
    cleantext = "".join(char for char in textchunk if char not in string.punctuation)
    words = set(cleantext.split())
    voc = sorted(words)
    return voc

def filterFuncWords(word_list, csv_file_path): #removes all func words
    # Read the CSV file and extract words
    filtered_list = []
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        word_set = set(row[0] for row in csv_reader)
    
    # Iterate through the word list and filter out words present in the CSV
    for word in word_list:
        if word not in word_set:
            filtered_list.append(word)
    return filtered_list

def get_all_articles():
    # get headlines
    #files = os.listdir("4-access-NYT/")
    #return files

    files = ["articles_2023-12.csv", "articles_2024-01.csv", "articles_2024-02.csv", "articles_2024-03.csv"]
    
    all_file_headlines = []
    for file in files:
        data = pd.read_csv(f"5-nyt-comparison/{file}")
        file_headlines = [row for row in data["lead_paragraph"]]
        for row in data["lead_paragraph"]:
            if type(row) is str:
                file_headlines = row
            else:
                file_headlines = ""
        headline_string = "".join(file_headlines)
        all_file_headlines.append(headline_string)

    return "".join(all_file_headlines)

    #convert everything into one string

        # for paragraph in data["lead_paragraph"]:
        #     if paragraph.isnan():
        #         text = ""
        #     else:
        #         text = paragraph.strip("“”")
        # all_headlines = all_headlines + pd.Series(text)

    # getUniqueWords
    #return all_headlines

print(get_all_articles())

# --------------------------------------------------

def get_transcriptions():
    data = pd.read_csv("4-get-transcriptions/filtered_w_transcription.csv")
    return data["transcription"]

def overlapList():

    # NYT ARTICLES
    
    article_words = getUniqueWords(get_all_articles()[0])
    article_filtered = filterFuncWords(article_words) 
    return article_filtered

    # embed article_filtered & cluster

    # TRANSCRIPTIONS
    # per video
    article_vector = text2vector(article_filtered,)

    for vid_transcript in get_transcriptions():
        # vector of 
        voc = getVocabulary(vid_transcript)
        vectorize = text2vector(vid_transcript, voc)
        
        #cosine_sim(vid_transcript, article vector)

    return cosine_sim

#print(overlapList())

# FOR TRANSCRIPT -----------
def text2vector(sentence, voc):
    """Given a sentence and the vocabulary for the problem,
    turn every sentence into a vector.
    """
    cleantext = "".join(char for char in sentence if char not in string.punctuation)
    words = cleantext.lower().split()
    vector = [words.count(w) for w in voc]
    return vector

def getVocabulary(textchunk):
    """Given some text, create the vocabulary of unique words."""
    textchunk = textchunk.lower()
    cleantext = "".join(char for char in textchunk if char not in string.punctuation)
    words = set(cleantext.split())
    voc = sorted(words)

    return voc
# ----------------------------

def cosine_sim(vec1, vec2):
    v1 = np.array(vec1)
    v2 = np.array(vec2)
    return np.dot(v1, v2)/(norm(v1)*norm(v2))