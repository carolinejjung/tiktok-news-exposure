# Using API Key to scrape NY Times
import requests

myAPIkey = "AYO8hb828roPgiJEA88Nqr4KAG7T3mgW" # CHANGE ME!
# Caroline: "AYO8hb828roPgiJEA88Nqr4KAG7T3mgW"

year = 2024
month = 2

URL = f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={myAPIkey}"

#data = requests.get(URL)
#articles = data.json()
#print(articles["response"]["docs"][0])


# -------------------------------------------------------------------------
# goal: Generate files with the list of videos from TikTok data
import json

def get_links(file):
  with open(file, 'r') as myFile:
    data = json.load(myFile)
  myFile.close()

  all_links = []
  feed = data["Activity"]["Favorite Videos"]["FavoriteVideoList"] #change the last two [] to be ["Video Browsing History"]["VideoList"]
  for i in range(len(feed)):
    link = feed[i]["Link"] #links of video --> need to scrape this later
    all_links.append(link)
  
  return all_links

print(get_links("user_data.json"))

# scrape info (video data, comments) & stores them in json files

