# install whisper first: pip install -U openai-whisper
# install open ai: pip install openai

from openai import OpenAI

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

# client = OpenAI()
# OpenAI.api_key = os.getenv('WHISPER_API_KEY')

client = OpenAI()

def transcribe_vid(file):
    audio_file = open(file, "rb")
    transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
    return transcription.text


# testfile = "4-get-transcriptions/mp4-files/share_video_7062567867182714158_.mp4"
# print(transcribe_vid(testfile))

# 50 requests per minute limit - sleep 1 second after each request
# don't run yet -- just do two columns


def get_all_transcriptions():
    files = os.listdir("4-get-transcriptions/mp4-files/")[:2]
    print(files)
    
    # for file in files:
    #     transcribe_vid(file)

print(get_all_transcriptions())
#testfile = "4-get-transcriptions/mp4-files/share_video_7062567867182714158_.mp4"
#print(transcribe_vid(testfile))