# install whisper first: pip install -U openai-whisper
# install open ai: pip install openai

from openai import OpenAI
from openai import APIStatusError
import pandas as pd
import time
import numpy as np

# pip install python-decouple
# from decouple import config
# API_KEY = config('WHISPER_API_KEY')
# client = OpenAI(api_key=API_KEY)

# pip install python-dotenv
# from dotenv import load_dotenv
# import os
# dotenv_path=".env"
# load_dotenv(dotenv_path)
# WHISPER_API_KEY = os.environ.get("WHISPER_API_KEY")

import os
API_KEY = os.getenv("WHISPER_API_KEY")  
client = OpenAI(api_key=API_KEY)

# client = OpenAI(api_key="OPENAI_API_KEY")

def transcribe_vid(file):
    audio_file = open(file, "rb")
    transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
    return transcription.text


def get_transcription_for_file(file, user): # for one file
    mp4_path = f"4-get-transcriptions/mp4-files-{user}/"

    try:
        transcription = transcribe_vid(mp4_path + file)
        time.sleep(1)
        print("SUCCESS: Video was transcribed.") # already done transcribing
        return transcription
    
    except APIStatusError:
        print("FAILURE: Video file size was too big to be transcribed. An empty transcription will be returned.")
        return ""
    
def data_to_write(user): # for one user
    mp4_path = f"4-get-transcriptions/mp4-files-{user}/"
    files = os.listdir(mp4_path)

    data = pd.read_csv(f"3-filter-metadata/news_relevant_videos_{user}.csv")

    transcripts_all = []
    for file in files: 
        transcripts_all.append(get_transcription_for_file(file, user))
    
    #append all the batches of transcriptions together into one flattened list with strings
    flattened_list_transcript = [transcript for transcript in transcripts_all]
    data["transcription"] = flattened_list_transcript
    return data

# TESTING
# print(get_all_transcriptions(create_batches("48271")[0], "48271")) # batch size 2
# print(get_all_transcriptions(create_batches("69117")[1], "69117"))

# TO RUN
path_to_write = '4-get-transcriptions/final-data-transcribed/'
# data_to_write("26301").to_csv(path_to_write + 'final_26301.csv') # TO DO
# data_to_write("33534").to_csv(path_to_write + 'final_33534.csv') # TO DO
# data_to_write("38129").to_csv(path_to_write + 'final_38129.csv') # DONE
data_to_write("48271").to_csv(path_to_write + 'final_48271.csv') # DONE
# data_to_write("69117").to_csv(path_to_write + 'final_69117.csv') # TO DO
# data_to_write("83721").to_csv(path_to_write + 'final_83721.csv') # RUN LAST (more videos)
