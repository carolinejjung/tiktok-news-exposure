import requests
import pandas as pd
import numpy as np
import os
import re
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from numpy.linalg import norm

file = "combined_articles.csv"  # Output file name
df = pd.read_csv(file)

lead_paragraphs_list = df["lead_paragraph"].dropna().tolist()

def filterFuncWords(input_string): #removes all func words
    # filtered_list = [] #represents unique words from tikTok
    # with open(csv_file_path, 'r') as file:
    #     csv_reader = csv.reader(file)
    #     word_set = set(row[0] for row in csv_reader)
    
    # # Iterate through the word list and filter out words present in the CSV
    # for word in v1:
    #     if word not in word_set:
    #         filtered_list.append(word)
    # return filtered_list #list w/ no stop words

    words = input_string.split()    
    filtered_words = [word for word in words if word not in function_words_set]
    result_string = ' '.join(filtered_words)
    return result_string

    #take in a vector, compare to words on stopwords.csv, filter out all common words, return unique words as vector


file_path = '/Users/sandyliu/tiktok-news-exposure/4-access-NYT/stopword_new.txt'
function_words_set = set()

with open(file_path, 'r') as file:
    for line in file:
        function_words_set.add(line.strip())
print(function_words_set)


cleaned_paragraphs = []
text_chunk = ""

##This is only for NYT stuff
for p in lead_paragraphs_list:
    p = filterFuncWords(p) #first filter out all the func words through this line
    text_chunk += p
    cleaned_paragraphs.append("".join(char for char in p if char not in string.punctuation))

#filter out puncs
text_chunk_cleaned = "".join(char for char in text_chunk if char not in string.punctuation)


## This function turn the whole text into a vec of unique words
def getVocabulary(textchunk):
    """Given some text, create the vocabulary of unique words."""
    textchunk = textchunk.lower()
    cleantext = "".join(char for char in textchunk if char not in string.punctuation)
    words = set(cleantext.split())
    voc = sorted(words)
    return voc

voc = getVocabulary(text_chunk_cleaned)

## This compare a sentence of the whole vector of words
def text2vector(sentence, voc):
    """Given a sentence and the vocabulary for the problem,
    turn every sentence into a vector.
    """
    cleantext = "".join(char for char in sentence if char not in string.punctuation)
    words = cleantext.lower().split()
    vector = [words.count(w) for w in voc]
    return vector

sent2vec = [text2vector(sent, voc) for sent in cleaned_paragraphs]
#sent2vec
 

#v1 should be a string, csv_file_path 



df = pd.DataFrame(sent2vec, 
                  columns=voc,
                  index=[f"doc_{i+1}" for i in range(len(sentences))])
df

# Here we get to the transcriptions
transcriptions = pd.read_csv('4-get-transcriptions/filtered_w_transcription.csv')

def cosineSimilarity(vec1, vec2):
    """Calculate the cosine similarity between two vectors."""
    V1 = np.array(vec1)
    V2 = np.array(vec2)
    cosine = np.dot(V1, V2)/(norm(V1)*norm(V2))
    return cosine