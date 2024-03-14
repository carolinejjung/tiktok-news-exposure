import requests

myAPIkey = "" #sandy

def get_NYT_articles(start_year, end_year):
    for year in range(start_year, end_year):
        for month in range(1, 13):
            URL = f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={myAPIkey}"
            print(URL)

            data = requests.get(URL)
            data.status_code