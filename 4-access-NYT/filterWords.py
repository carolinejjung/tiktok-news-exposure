import requests, json
import pandas as pd
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
    pd.read_csv()

def overlapList(list1, ):

    # all_headlines = all article headlines

    article_words = getUniqueWords(all_headlines)
    article_filtered = filterFuncWords(article_words) #list 1

    # embed article_filtered & cluster

    transcriptions