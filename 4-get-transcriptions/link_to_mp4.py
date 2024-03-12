import pyktok as pyk
import json


filepath = "3-filter-metadata/new_relevant_videos.csv"
with open(filepath, "r") as filetoread:
    list_of_dict = json.load(filetoread)
filetoread.close()

links = [video_dict["link"] for video_dict in list_of_dict]
print(links)
# note: last video is "unavailable"

# same issue with KeyError: 'itemInfo'
# developers: https://github.com/dfreelon/pyktok/blob/main/src/pyktok/pyktok.py


# using developer's functions
pyk.specify_browser('chrome') 
pyk.save_tiktok_multi_urls(links,False,'mp4_files/tiktok_data.csv',1)

# using for loop
# for link in links:
#     pyk.specify_browser('chrome') 
#     pyk.save_tiktok(link, True, 'video_data.csv','chrome')

# another potential issue: all mp4 files get saved to the main directory and we cannot put it in the mp4_files folder