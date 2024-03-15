import requests, json
import pandas as pd
from collections import Counter
import os

myAPIkey = 'CYJUbGC4TcnBoLg8PF1HlnEhJEEPHlBv' #maya 

'''
def get_NYT_articles(start_year, end_year):
    for year in range(start_year, end_year):
        for month in range(1, 13):
            URL = f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={myAPIkey}"
            print(URL)

            data = requests.get(URL)
            data.status_code

'''
def getNYTArticles(year, month, apiKey):
    """Function that sends a request to the NYT API for all articles in a month
    and then stores the results in a JSON file.
    """
    # create URL
    URL = f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={apiKey}"

    # send the request to get the data
    data = requests.get(URL)
    if data.status_code == 200:
        print("Successfully got the data.")

    dataJson = data.json() # get response as JSON

    with open(f"NYT_{year}-{month}.json", 'w') as fout:
        json.dump(dataJson, fout)

def getArticlesOfDay(date):
    year = int(date[:4])
    #print(year)
    month = int(date[5:7]) if date[5] == '0' else int(date[5:7])
    #print(month)
    file_name = f"NYT_{year}-{month}.json"
    if os.path.exists(file_name):  # Check if CSV file exists
        print("found file!")
        pass
    else:
        getNYTArticles(year, month, myAPIkey)

    with open(f"NYT_{year}-{month}.json") as fin:
        data = json.load(fin)

    articles = data['response']['docs']

    articles_day = []
    dates_list = []  # List to store publication dates

    for article in articles:
        pub_date = article['pub_date'][:10]  # Extracting publication date
        dates_list.append(pub_date)  # Add the publication date to the list
        if pub_date == date:
            articles_day.append(article)

    #print("Publication Dates:", dates_list)  # Print list of publication dates
    return articles_day


def flattenArticle(article):
    output_dict = {}
    things_to_get = ['abstract', 'lead_paragraph', 'headline', 'keywords', 'pub_date', 'document_type', 'section_name']
    for info in things_to_get:
        output_dict[info] = article[info]
    keywords = output_dict['keywords']
    keywords = [tag['value'] for tag in keywords] 
    output_dict['keywords'] = keywords
    return output_dict

def flattenAllArticles(date):
    articles_of_the_day = getArticlesOfDay(date)
    output_list = []
    for article in articles_of_the_day:
        output_list.append(flattenArticle(article))
    
    df = pd.DataFrame(output_list)
    file_name = f"articles_{date[:7]}.csv"
    df.to_csv(file_name, index=False)
    return df

desired_date = "2024-01-06"
articles = flattenAllArticles(desired_date)
#print(len(articles))