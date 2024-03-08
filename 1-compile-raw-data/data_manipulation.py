# goal: Generate files with the list of videos from TikTok data
import json
import os

def get_all_links(file):
  all_links = []
  
  file_name = dir_path + "/" + file
  with open(file_name, 'r') as myFile:
    data = json.load(myFile)
  myFile.close()

  feed_dict = data["Activity"]["Video Browsing History"]
  if feed_dict == {}:
    print("this file has NO video list")
    return []
  else:
    feed = feed_dict["VideoList"]
    for i in range(len(feed)):
      all_links.append(feed[i])
  return all_links

def create_user_json(files):
  for file in files:
    data = get_all_links(file)
    initial = file[10:12]
    with open(f"1-compile-raw-data/user_data_{initial}.json", "w") as file_to_write:
      json.dump(data, file_to_write)
    file_to_write.close()

dir_path = '/users/carolinejung/cs315-private/project2-files' # hardcoded for security purposes
files = os.listdir(dir_path)
create_user_json(files)

