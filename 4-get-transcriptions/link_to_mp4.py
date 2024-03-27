import pyktok as pyk
import pandas as pd

def save_mp4(filepath, user):
    # both parameters are strings
    data = pd.read_csv(filepath)

    data["link"] = [f"https://www.tiktokv.com/share/video/{id}/" for id in data["video_id"]]

    pyk.specify_browser('chrome')
    pyk.save_tiktok_multi_urls(video_urls=data["link"],save_video=True,metadata_fn=f'mp4-files/tiktok_data.csv',
                               sleep=1, browser_name="chrome", usernum=user)

# FINAL
# user RB data chunks (83721)
# save_mp4("3-filter-metadata/news_relevant_videos_chunk_3.csv", "83721") # DONE
# save_mp4("3-filter-metadata/news_relevant_videos_chunk_4.csv", "83721") # DONE
# save_mp4("3-filter-metadata/news_relevant_videos_chunk_5.csv", "83721") # DONE

# other users
# save_mp4("3-filter-metadata/news_relevant_videos_26301.csv", "26301") # DONE
# save_mp4("3-filter-metadata/news_relevant_videos_33534.csv", "33534") # DONE
# save_mp4("3-filter-metadata/news_relevant_videos_38129.csv", "38129") # DONE
#save_mp4("3-filter-metadata/news_relevant_videos_48271.csv", "48271") # HOLD - VIDEO ID STRUCTURED DIFF, FROM SEC 1
save_mp4("3-filter-metadata/news_relevant_videos_69117.csv", "69117") # TO DO


# TESTING
#save_mp4("3-filter-metadata/new_relevant_videos.csv")