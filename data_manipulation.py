# Using API Key to scrape NY Times
import requests
import os, csv

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

def get_all_links():
  files = os.listdir('all_data')
  print(files)
  print(len(files))
  all_links = []


  for file in files:
    print(file)
    file_name = 'all_data/' + file
    with open(file_name, 'r') as myFile:
      data = json.load(myFile)
    myFile.close()

    print(data)
    feed = data["Activity"]["Favorite Videos"]["FavoriteVideoList"] #change the last two [] to be ["Video Browsing History"]["VideoList"]
    if feed == None:
      print("this file has NO video list")
    else:
    #print(feed)
      for i in range(len(feed)):
        link = feed[i]["Link"] #links of video --> need to scrape this later
        all_links.append(link)
  
  return all_links

links = get_all_links()
print('links: ', links)


  

#print(get_links("all_data/user_data_CJ.json"))



# scrape info (video data, comments) & stores them in json files

