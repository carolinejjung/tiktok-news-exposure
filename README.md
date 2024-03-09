# tiktok-news-exposure
CS 315 Project on analyzing the amount of news exposure on TikTok. 

By: Caroline Jung, Sophie Hwang, Maya Lu-Heda, Sandy Liu, Josie, Ryan


## How to collect metadata
### Step 1: create virtual environment
1. cd into the folder: `cd 2-collect-metadata-pyktok`
2. create new environment within this folder: `python -m venv .project2`
3. activate environment: `source .project2/bin/activate`; for Windows: `.project2/Scripts/activate`
4. install packages in pyktok: `pip install -r requirements.txt`
5. cd out of the folder back into main directory: `cd ..` \
    At this point, your terminal should look like this:
    ![terminal](image-1.png)

### Step 2: run code to collect metadata
If running full json file:
`python 2-collect-metadata-pyktok/pyktok-collect.py 1-compile-raw-data/user_data_CJ.json 2-collect-metadata-pyktok/CJ_metadata.csv`

If running split up json file (in chunks):
`python 2-collect-metadata-pyktok/pyktok-collect.py 1-compile-raw-data/rb_data_chunks/user_data_rb_chunk_1.json 2-collect-metadata-pyktok/final-metadata/RB-chunks/RB_chunk_1_metadata.csv`

**IMPORTANT AND CRUCIAL MODIFICATION:** replace file names and chunk numbers with the appropriate ones you want to run and save! Make sure you're running the code on the correct files.

Chunk 1 of RB's data will have:
- Input file: 1-compile-raw-data/rb_data_chunks/user_data_rb_chunk_1.json
- Output file: 2-collect-metadata-pyktok/final-metadata/RB-chunks/RB_chunk_1_metadata.csv

Chunk 2 of RB's data should have:
- Input file: 1-compile-raw-data/rb_data_chunks/user_data_rb_chunk_2.json
- Output file: 2-collect-metadata-pyktok/final-metadata/RB-chunks/RB_chunk_2_metadata.csv

and etc. for all chunks (just change chunk number within the file names)


### Step 3: check csv files
Once you run, you should output 2 new files: `...metadata.csv` and `failed.csv` (videos that could not be located). These files should be in the following paths with the following naming convention:
- 2-collect-metadata-pyktok/final-metadata/RB-chunks/**initial**_chunk\_**num**_metadata.csv
- 2-collect-metadata-pyktok/failed/failed_**initial**_chunk\_**num**.csv

**IMPORTANT AND CRUCIAL STEP: RENAME YOUR `failed.csv` FILE BEFORE PUSHING!!** In the bolded area, replace the initial and chunk number of the file you ran to make it look like `failed_RB_chunk_1.csv` for chunk 1 of RB's data. You must do this step to not overwrite other user data and chunk numbers. 

Also, make sure that the csv's are located in the correct folders. If not, place it in the correct location (see bullets above).
