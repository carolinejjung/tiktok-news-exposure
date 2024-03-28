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


def get_all_transcriptions(batch, user):
    mp4_path = f"4-get-transcriptions/mp4-files-{user}/"

    transcripts = []
    try:
        for file in batch:
            transcripts.append(transcribe_vid(mp4_path + file))
            time.sleep(1)
        print("Batch of videos is able to be transcribed. Transcribing...")
        return transcripts
    
    except APIStatusError:
        print("File size is too big to be able to transcribe. Empty transcriptions will be returned. Moving onto the next batch...")
        return ["",""]

def create_batches(user):
    mp4_path = f"4-get-transcriptions/mp4-files-{user}/"
    files = os.listdir(mp4_path)

    even_nums = np.array(range(0,len(files)+1,2)) #list of even indices, experiment w max size

    batches = []
    for i in range(len(even_nums)):
        if i != len(even_nums)-1:
            batches.append(files[even_nums[i]:even_nums[i+1]])
    return batches
    
def data_to_write(user):
    batches = create_batches(user)
    data = pd.read_csv(f"3-filter-metadata/news_relevant_videos_{user}.csv")

    transcript_batches = []
    for i in range(len(batches)):  # range(3) was used for testing purposes
        transcript_batches.append(get_all_transcriptions(batches[i], user))
    
    #append all the batches of transcriptions together into one flattened list with strings
    flattened_list_transcript = [transcript for batch in transcript_batches for transcript in batch]
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
# data_to_write("48271").to_csv(path_to_write + 'final_48271.csv') # DONE
# data_to_write("69117").to_csv(path_to_write + 'final_69117.csv') # TO DO
# data_to_write("83721").to_csv(path_to_write + 'final_83721.csv') # RUN LAST (more videos)

