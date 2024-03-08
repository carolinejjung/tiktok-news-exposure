# goal: Generate files with the list of videos from TikTok data
import json
import os

def get_all_links():
  dir_path = '/users/carolinejung/cs315-private/project2-files' # hardcoded for security purposes
  files = os.listdir(dir_path)

  all_links = []
  for file in files:
    print(file)
    file_name = dir_path + "/" + file
    with open(file_name, 'r') as myFile:
      data = json.load(myFile)
    myFile.close()

    feed_dict = data["Activity"]["Video Browsing History"]

    if feed_dict == {}:
      print("this file has NO video list")
    else:
      feed = feed_dict["VideoList"]
      for i in range(len(feed)):
        link = feed[i]["Link"]
        all_links.append({"link": link})
  
  return all_links

data = get_all_links()

# write video links to separate json file
with open("compiled_data.json", "w") as file_to_write:
    json.dump(data, file_to_write)

