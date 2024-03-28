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
        transcription = transcribe_vid(mp4_path + file) # transcribe video
        time.sleep(1)
        print("SUCCESS: Video was transcribed.")
        return transcription
    
    except APIStatusError:
        print("FAILURE: Video file size was too big to be transcribed. An empty transcription will be returned.")
        return ""
    
def data_to_write(user): # for one user
    """This method only transcribes videos that were actually downloaded as mp4 files. These videos are already
    filtered and considered as news-relevant videos."""

    mp4_path = f"4-get-transcriptions/mp4-files-{user}/"
    files = os.listdir(mp4_path)

    file_data = []
    for file in files: 
        # note: this for loop does not go through each video in order of id number
        filename = file[12:31] # string
        transcription = get_transcription_for_file(file, user) # string
        file_data.append([filename, transcription])

    summary = pd.DataFrame(file_data, columns=["VideoID", "Transcription"])
    return summary

    # #append all the batches of transcriptions together into one flattened list with strings
    # flattened_list_transcript = [transcript for transcript in transcripts_all]
    # print("Transcript:", flattened_list_transcript)
    # data["transcription"] = flattened_list_transcript
    # return data
    

# TESTING
# print(get_all_transcriptions(create_batches("48271")[0], "48271")) # batch size 2
# print(get_all_transcriptions(create_batches("69117")[1], "69117"))

# TO RUN
path_to_write = '4-get-transcriptions/final-data-transcribed/'
# data_to_write("26301").to_csv(path_to_write + 'final_26301.csv') # TO DO


data_to_write("33534").to_csv(path_to_write + 'final_33534.csv') # TO DO - initial error: length of values(64) doesn't match length of index (70)
# data_to_write("38129").to_csv(path_to_write + 'final_38129.csv') # TO DO - should be empty
# data_to_write("48271").to_csv(path_to_write + 'final_48271.csv') # DONE
# data_to_write("69117").to_csv(path_to_write + 'final_69117.csv') # TO DO
# data_to_write("83721").to_csv(path_to_write + 'final_83721.csv') # RUN LAST (more videos)

# TEST
#print(data_to_write("48271"))
#data_to_write("48271").to_csv(path_to_write + 'test_48271.csv') # DONE
