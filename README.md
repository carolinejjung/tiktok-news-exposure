# tiktok-news-exposure
CS 315 Project on analyzing the amount of news exposure on TikTok. 

By: Caroline Jung, Sophie Hwang, Maya Lu-Heda, Sandy Liu, Josie, Ryan


## How to collect metadata
### Step 1: create virtual environment
1. cd into the folder: `cd 2-collect-metadata-pyktok`
2. create new environment within this folder: `python -m venv .project2`
3. activate environment: `source .project2/bin/activate`
4. install packages in pyktok: `pip install -r requirements.txt`
5. cd out of the folder back into main directory: `cd ..`
    At this point, your terminal should look like this:
    ![terminal](image-1.png)

### Step 2: run code to collect metadata
If running full json file:
`python 2-collect-metadata-pyktok/pyktok-collect.py 1-compile-raw-data/user_data_CJ.json 2-collect-metadata-pyktok/rb_chunk_1_metadata.csv`

If running split up json file (in chunks):
`python 2-collect-metadata-pyktok/pyktok-collect.py 1-compile-raw-data/rb_data_chunks/user_data_rb_chunk_1.json 2-collect-metadata-pyktok/rb_chunk_1_metadata.csv`

Note: replace file names with the appropriate ones you want to run and save!