import os
import json
print("Current Directory:", os.getcwd())
file_name = "user_data_rb"

def split_json(input_file, chunk_size=10000):
    output_folder = '/Users/sandyliu/tiktok-news-exposure/1-compile-raw-data/rb_data_chunks'

    with open(input_file, 'r') as f:
        data = json.load(f)

    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    
    for i, chunk in enumerate(chunks):
        output_file = os.path.join(output_folder, f'{file_name}_chunk_{i+1}.json')
        with open(output_file, 'w') as f:
            json.dump(chunk, f, indent=4) 
    
        print(f'Chunk {i+1} saved to {output_file}')

input_file = '/Users/sandyliu/tiktok-news-exposure/1-compile-raw-data/user_data_rb.json'
split_json(input_file)