import json

path = "1-compile-raw-data/compiled_data.json"
with open(path, "r") as file:
    data = json.load(file)

print(len(data))