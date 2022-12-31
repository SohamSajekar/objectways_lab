import uvicorn
from fastapi import FastAPI
from utils.util import read_convert_to_jsonl, count_entities, save_csv


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the API home page!",
            "services": {1: "/get_entities", 2: "/transform_json_to_csv"}}

@app.get("/get_entities")
def function_get_entities(data: dict):
    _, _, _, final = count_entities(data)
    return final

@app.get("/transform_json_to_csv/{file_path}")
def function_transform_json_to_csv(file_path: str):
    data = read_convert_to_jsonl(file_path)
    filenames, entity_types, entity_count = [], [], []
    for file in data:
        fnames, etypes, count, _ = count_entities(file)
        filenames.append(fnames)
        entity_types.append(etypes)
        entity_count.append(count)
    saved_path, _ = save_csv(filenames, entity_types, entity_count)
    return {"Saved path to csv": file_path, "output": saved_path}

if __name__ == '__main__':
    uvicorn.run(app, port=8000)