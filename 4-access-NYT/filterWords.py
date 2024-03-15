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

def get_transcriptions():
    data = pd.read_csv("4-get-transcriptions/filtered_w_transcription.csv")
    return data["transcription"]

def get_all_articles():
    #files = os.listdir("4-access-NYT/")
    #return files
    all_articles = []

    
    with open("5-nyt-comparison/articles_data/articles_2013-12-16.csv") as file1:
        f1 = json.load(file1)
    with open("5-nyt-comparison/articles_data/articles_2013-12-17.csv") as file2:
        f2 = json.load(file2)
    
    all_articles.append(f1)
    all_articles.append(f2)
    return all_articles

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

print(overlapList())

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