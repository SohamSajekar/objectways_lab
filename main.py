import os
import uvicorn
from fastapi import FastAPI
from utils.util import read_convert_to_jsonl, count_entities, save_csv


# Create/Initialize App
app = FastAPI()

# Simple get method for api-root: enlists available services
@app.get("/")
async def root():
    return {"message": "Welcome to the API home page!",
            "services": {1: "/get_entities", 2: "/transform_json_to_csv"}}

# Service-1: /get_entities, requests a json payload and parses its entities "type" with their counts
@app.post("/get_entities")
def function_get_entities(data: dict):
    # Parse json object and fetch entity 'type' along with counts
    _, _, _, final = count_entities(data)
    return final

# Service-2: /transform_json_to_csv, requests json file path and generates csv data, returning csv save path
@app.post("/transform_json_to_csv/{file_path}")
def function_transform_json_to_csv(file_path: str):

    # Load and convert json to jsonl
    data = read_convert_to_jsonl(file_path)
    filenames, entity_types, entity_count = [], [], []

    # Iterate over all json-lines of json object
    for file in data:
        # Fetch csv information
        fnames, etypes, count, _ = count_entities(file)
        filenames.append(fnames)
        entity_types.append(etypes)
        entity_count.append(count)

    # Create and save csv file
    saved_path, _ = save_csv(filenames, entity_types, entity_count)
    saved_path = os.getcwd() + '/' + saved_path

    return {"Saved path to csv": saved_path}


if __name__ == '__main__':
    uvicorn.run(app, port=8000)