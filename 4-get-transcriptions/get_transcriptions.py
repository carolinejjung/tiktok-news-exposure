# install whisper first: pip install -U openai-whisper
# install open ai: pip install openai

from openai import OpenAI
import pandas as pd

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
# API_KEY = os.getenv("WHISPER_API_KEY")  
# client = OpenAI(api_key=API_KEY)

client = OpenAI()

def transcribe_vid(file):
    audio_file = open(file, "rb")
    transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
    return transcription.text

def get_all_transcriptions():
    mp4_path = "4-get-transcriptions/mp4-files/"
    files = os.listdir(mp4_path)[:2]
    data = pd.read_csv("3-filter-metadata/new_relevant_videos.csv")
    #data["transcription"] = [transcribe_vid(mp4_path+file) for file in files] 
    # REPLACE WITH THIS LATER
    # 50 requests per minute limit - sleep 1 second after each request

    # create new temporary dataframe
    new = data.iloc[0:2, 1:].copy()
    new["transcription"] = [transcribe_vid(mp4_path+file) for file in files]

    return new

get_all_transcriptions().to_csv('4-get-transcriptions/filtered_w_transcription.csv')