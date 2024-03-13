import pyktok as pyk
import pandas as pd

data = pd.read_csv("3-filter-metadata/new_relevant_videos.csv")
data["link"] = [f"https://www.tiktokv.com/share/video/{id}/" for id in data["video_id"]]

pyk.specify_browser('chrome') 
pyk.save_tiktok_multi_urls(data["link"],False,'mp4_files/tiktok_data.csv',1)