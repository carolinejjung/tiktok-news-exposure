import requests
import pandas as pd
import numpy as np
import os
import re
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

file = "combined_articles.csv"  # Output file name
df = pd.read_csv(file)

lead_paragraphs_list = df["lead_paragraph"].dropna().tolist()

cleaned_paragraphs = []
text_chunk = ""
for p in lead_paragraphs_list:
    text_chunk += p
    cleaned_paragraphs.append("".join(char for char in p if char not in string.punctuation))


text_chunk_cleaned = "".join(char for char in text_chunk if char not in string.punctuation)

#cleaned_pragraph -- the list of headlines without punc
#text_chunk -- without punc in huge string file

def getVocabulary(textchunk):
    """Given some text, create the vocabulary of unique words."""
    textchunk = textchunk.lower()
    cleantext = "".join(char for char in textchunk if char not in string.punctuation)
    words = set(cleantext.split())
    voc = sorted(words)
    return voc

voc = getVocabulary(text_chunk_cleaned)

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
 
 def filterFuncWords(v1, csv_file_path): #removes all func words
    filtered_list = [] #represents unique words from tikTok
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        word_set = set(row[0] for row in csv_reader)
    
    # Iterate through the word list and filter out words present in the CSV
    for word in v1:
        if word not in word_set:
            filtered_list.append(word)
    return filtered_list #list w/ no stop words

    #take in a vector, compare to words on stopwords.csv, filter out all common words, return unique words as vector









df = pd.DataFrame(sent2vec, 
                  columns=voc,
                  index=[f"doc_{i+1}" for i in range(len(sentences))])
df

# getVocabulary(" ".join(vocabulary))

# def text2vector(sentence, voc):
#     """Given a sentence and the vocabulary for the problem,
#     turn every sentence into a vector.
#     """
#     cleantext = "".join(char for char in sentence if char not in string.punctuation)
#     words = cleantext.lower().split()
#     vector = [words.count(w) for w in voc]
#     return vector


transcriptions = pd.read_csv('4-get-transcriptions/filtered_w_transcription.csv')


# sent2vec = [text2vector(sent, vocabulary) for sent in sentences]
# sent2vec
