# goal: Generate files with the list of videos from TikTok data
import json
import os

# FILES FOR DATE AND LINK (PUBLIC)
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

dir_path = '/users/carolinejung/cs315-private/project2-files/raw' # hardcoded for security purposes
files = os.listdir(dir_path)
create_user_json(files)

# FILES FOR FOLLOWER LIST (NON-PUBLIC)
def collect_following(file):
  file_name = dir_path + "/" + file
  with open(file_name, 'r') as myFile:
    data = json.load(myFile)
  myFile.close()

  following=[]
  followers = data["Activity"]["Following List"]
  if followers == {}:
    print("this user does not follow anyone")
    return []
  else:
    user = followers["Following"]
    for i in range(len(user)):
      following.append(user[i]["UserName"]) #date, username
  return following

def following_json(files):
  for file in files:
    data = collect_following(file)
    initial = file[10:12]
    filepath_to_write = f'/users/carolinejung/cs315-private/project2-files/user_data_{initial}_following.json'
    # note: we want to keep non-news accounts that users follow private
    with open(filepath_to_write, "w") as file_to_write:
      json.dump(data, file_to_write)
    file_to_write.close()

following_json(files)